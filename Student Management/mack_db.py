import sqlite3
def create_db():
    con=sqlite3.connect(database=r'sms.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll_no INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,address text)")
    con.commit()
    
    
create_db()