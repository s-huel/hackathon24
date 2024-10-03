import hashlib

def signup():
    email = input("E-mail adres: ")
    wachtwoord = input("Wachtwoord: ")
    bevestiging_wachtwoord = input("Bevestig wachtwoord: ")

    if bevestiging_wachtwoord == wachtwoord:
        enc = bevestiging_wachtwoord.encode()
        hash1 = hashlib.md5(enc).hexdigest()

        with open("student_inlog_data.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)

        print("Je account is aangemaakt")
    else:
        print("Wachtwoord komt niet overeen")


def login():
     email = input("E-mail adres: ")
     wachtwoord = input("Wachtwoord: ")
     auth = wachtwoord.encode()
     auth_hash = hashlib.md5(auth).hexdigest()
     with open("student_inlog_data.txt", "r") as f:
         stored_email, stored_wachtwoord = f.read().split("\n")
     f.close()
     if email == stored_email and auth_hash == stored_wachtwoord:
         print("Ingelogd")
     else:
         print("Inlog fout")