import mysql.connector
from fastapi import FastAPI, HTTPException

app = FastAPI()

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
            charset='utf8mb4',  # Specify utf8mb4 charset
            collation='utf8mb4_general_ci'  # Supported collation in older versions
        )
        cursor = connection.cursor()

        # 1. SQL query to fetch the student by email and password
        query = "SELECT * FROM `Student` WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        # Fetch one result for Student
        data = cursor.fetchone()

        # 2. If no student is found, check the Teacher table
        if data is None:
            query = "SELECT * FROM `Teacher` WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            data = cursor.fetchone()

        # 3. Always check the Admin table last
        query = "SELECT * FROM `Admin` WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        admin_data = cursor.fetchone()

        # 4. Replace the data with admin data if an admin is found
        if admin_data is not None:
            data = admin_data

        # 5. If no user (student, teacher, or admin) is found, raise an exception
        if data is None:
            raise HTTPException(status_code=404, detail="User not found")

        # 6. Return the data found (could be student, teacher, or admin)
        return {"data": data}

    except mysql.connector.Error as err:
        # Handle database connection errors
        raise HTTPException(status_code=500, detail="Database connection error: " + str(err))
    
    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
