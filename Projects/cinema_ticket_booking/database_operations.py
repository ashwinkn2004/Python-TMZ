import sqlite3



conn = sqlite3.connect("./Projects/cinema_ticket_booking/cinema.db")
cur = conn.cursor()



# Users table creation

def createUserTable():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS USERS(
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    

def checkUsername(username):
    cur.execute('''
        SELECT * FROM USERS WHERE username = ?
    ''', (username,))
    return cur.fetchone()



# User registration based on roles

def userRegisterInDb(username, password, role):
    cur.execute('''
            INSERT INTO USERS(username, password, role)
            VALUES(?, ?, ?)
        ''', (username, password, role))
    
    conn.commit()


def validateUser(username, password):
    cur.execute('''
            SELECT * FROM USERS WHERE username = ? AND password = ?
        ''', (username, password))
    
    return cur.fetchone()