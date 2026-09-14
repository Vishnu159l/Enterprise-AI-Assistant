import sqlite3
from pwdlib import PasswordHash



SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def user_exists(empid):
    conn = sqlite3.connect("EmployeeDatabase.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * 
        FROM Employee
        WHERE empId = (?); 
    """,(empid,),)
    res = cursor.fetchall()
    return res

def get_user_role(empid):
    conn = sqlite3.connect("EmployeeDatabase.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT role 
        FROM Employee 
        WHERE empId = (?)
    """,(empid,),)

    res = cursor.fetchone()
    return res

def get_user_hash(empid):
    conn = sqlite3.connect("EmployeeDatabase.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT password
        FROM Employee
        WHERE empId = (?);
    """,(empid,),)

    res = cursor.fetchall()
    return res

def add_user(name,password,role):
    hashed_password = get_password_hash(password)
    cursor.execute("""
        SELECT empId
        FROM Employee
        ORDER BY empID DESC
        LIMIT 1;
    """)

    id = cursor.fetchone()
    if id is None:
        id = (0,)
    cursor.execute("""
        INSERT INTO Employee
        VALUES (?,?,?,?);
    """,(id[0] + 1,name,hashed_password,role),)

def view_table():
    cursor.execute("SELECT * FROM Employee")
    for row in cursor.fetchall():
        print(row)

def get_user_data(id):
    conn = sqlite3.connect("EmployeeDatabase.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * 
        FROM Employee 
        WHERE empId = (?)
    """,(id,),)

    res = cursor.fetchone()
    return res
    
#cursor.execute("DROP TABLE Employee")

#cursor.execute("""
#REATE TABLE Employee (
#    empId int,
#    name varchar(30),
#    password varchar(30),
#    role varchar(30)
#
#""")

#cursor.execute("""
#INSERT INTO Employee 
#Values
#    (1,'Vishnu','Manid@159l','Admin'),
#    (2,'Akhil','asdfghjkl;','Hr'),
#    (3,'Prakash','nigger','Engineer');
#""")

#cursor.execute("SELECT * FROM Employee")
#print(cursor.fetchall())

#add_user('Vishnu','Manid@159l','Admin')
#add_user('Akhil','asdfghjkl;','Hr')
#add_user('Prakash','nigger','Engineer')
#delete_user(5)



#view_table()

#print(get_user_password_by_id(1))

#user = get_user_role("Vishnu","Manid@159l")
#print(user)

#conn.commit()

#conn.close()