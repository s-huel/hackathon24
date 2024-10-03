import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can restrict this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/login")
def login(email: str, password: str):
    # Connect to the database
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            user='bit_academy',  # Your MySQL username
            password='bit_academy',  # Your MySQL password
            host='localhost',
            database='Lerend_Kwalificeren',
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        cursor = connection.cursor()

        # SQL query to fetch the student by email and password
        role = "Student"
        isAdmin = False
        query = "SELECT * FROM `Student` WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        # Fetch one result
        data = cursor.fetchone()

        if data is None:
            query = "SELECT * FROM `Teacher` WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            data = cursor.fetchone()
            role = "Teacher"

            query = "SELECT * FROM `Admin` WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            dataAdmin = cursor.fetchone()

            if dataAdmin is not None:
                data += dataAdmin
                isAdmin = True

            if data is None:
                raise HTTPException(status_code=404, detail="User not found")

        return {"data": data, "role": role, "isAdmin": isAdmin}
    
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Database connection error" + str(err))
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
