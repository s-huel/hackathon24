import mysql.connector
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/login")
def login(email: str, password: str):
    # Connect to the database
    try:
        connection = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',
            database='Lerend_Kwalificeren'
        )
        cursor = connection.cursor()

        # SQL query to fetch the student by email and password
        cursor.execute("SELECT * FROM `Student` WHERE email = %s AND password = %s", (email, password))

        # Fetch one result
        data = cursor.fetchone()

        # If no user is found, raise an exception
        if data is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Return the data found
        return {"data": data}

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database connection error: {err}")
    
    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
