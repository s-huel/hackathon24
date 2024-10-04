
from mysql.connector import pooling, Error
import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can restrict this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

connection = mysql.connector.connect(
    user='bit_academy',
    password='bit_academy',
    host='localhost',
    database='Lerend_Kwalificeren',
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)

# Update criterium for a student
@app.post("/update_criterium/{student_id}/{criterium_id}")
async def update_criterium(student_id: int, criterium_id: int, number: int):
    try:
        connection = connection.cursor()
        cursor = connection.cursor()

        # Update the number associated with the criterium
        update_query = """
            UPDATE student_criteria 
            SET number = %s 
            WHERE student_id = %s AND id = %s
        """
        cursor.execute(update_query, (number, student_id, criterium_id))
        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Criterium not found")
        
        return {"message": "Criterium updated successfully"}
    
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    
    finally:
        cursor.close()
        connection.close()


@app.post("/check_done/{student_id}")
async def check_done(student_id: int):
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Fetch all criteria for the student
        select_query = """
            SELECT number FROM student_criteria WHERE student_id = %s
        """
        cursor.execute(select_query, (student_id,))
        criteria_list = cursor.fetchall()

        if not criteria_list:
            raise HTTPException(status_code=404, detail="No criteria found for this student")

        # Count occurrences of 6 and 7
        count_six = sum(1 for c in criteria_list if c['number'] == 6)
        count_seven = sum(1 for c in criteria_list if c['number'] == 7)

        # Business logic to mark as done
        if count_six >= 3 and count_seven >= 3:
            # Mark the student as done in the database
            update_query = """
                UPDATE students 
                SET is_done = TRUE 
                WHERE id = %s
            """
            cursor.execute(update_query, (student_id,))
            connection.commit()

            return {"message": f"Student {student_id} marked as done"}
        else:
            return {"message": f"Student {student_id} does not meet the criteria yet"}
    
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)