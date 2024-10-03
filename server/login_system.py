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

        # SQL query to fetch the student by email and password
        query = "SELECT * FROM `Student` WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        # Fetch one result
        data = cursor.fetchone()

        # If no student is found, repeat for teacher
        if data is None:
            query = "SELECT * FROM `Teacher` WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            data = cursor.fetchone()

            query = "SELECT * FROM `Admin` WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            dataAdmin = cursor.fetchone()
            
            if dataAdmin is not None:
                data = dataAdmin
            
            if data is None and dataAdmin is None:
                # If no student or teacher is found, return an error
                raise HTTPException(status_code=404, detail="User not found")

        # Return the data found
        return {"data": data}
    
    except mysql.connector.Error as err:
        # Handle database connection errors
        raise HTTPException(status_code=500, detail="Database connection error" + str(err))
    
    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
