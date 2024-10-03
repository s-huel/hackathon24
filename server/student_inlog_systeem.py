from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/student_inlog_systeem")
async def login_student(email: str, password: str):
    if email != "correct_email@example.com":
        raise HTTPException(status_code=400, message="E-mail address klopt niet")
    
    if password != "correct_password":
        raise HTTPException(status_code=400, message="Wachtwoord klopt niet")

    return {"message": "Succesvol ingelogd"}

