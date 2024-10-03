import re
import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialisatie van de FastAPI-app
app = FastAPI()

# Functie om een te kijken of het echt een email adress is
def email_is_valid(email: str) -> bool:
    email_pattern = r"^\S+@\S+\.\S+$"
    return re.match(email_pattern, email) is not None

# Databaseconfiguratie
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'Lerend_Kwalificeren'
}

# Pydantic-model voor gebruikerslogin
class UserLogin(BaseModel):
    user_type: str
    email: str
    password: str

# Functie om gebruikersinformatie uit de database op te halen
def pull_user(user_type: str, email: str, password: str):
    # Check het e-mailadres
    if not email_is_valid(email):
        raise ValueError("Vul een email adres in")

    try:
        # Verbinding maken met de database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL-query voorbereiden op basis van gebruikersrol en e-mail
        query = "SELECT * FROM users WHERE role = %s AND email = %s"
        cursor.execute(query, (user_type, email))

        # Gegevens van de gebruiker ophalen
        user_data = cursor.fetchone()
        if not user_data:
            raise LookupError("Onjuiste e-mail")

        # Controleer het wachtwoord
        stored_password = user_data[3]
        if not check_password(password, stored_password):
            raise ValueError("Onjuist wachtwoord")

        # Retourneer relevante gebruikersinformatie
        return {
            'user_id': user_data[0],
            'role': user_data[1],
            'email': user_data[2],
        }

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Databasefout: {err}")

    finally:
        # Sluit de databaseverbinding
        cursor.close()
        conn.close()

# Functie om het wachtwoord te controleren (implementatie van hashing hier toevoegen)
def check_password(input_password: str, stored_password: str) -> bool:
    return input_password == stored_password  # Vervang dit door daadwerkelijke hash-controle

# FastAPI-eindpunt voor gebruikerslogin
@app.post("/login")
async def login(user: UserLogin):
    try:
        # Probeer de gebruiker op te halen en in te loggen
        user_info = pull_user(user.user_type, user.email, user.password)
        return {"message": "Login succesvol", "user_info": user_info}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except LookupError as le:
        raise HTTPException(status_code=404, detail=str(le))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Start de applicatie
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
