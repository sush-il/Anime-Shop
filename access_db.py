import sqlite3

conn = sqlite3.connect('info.db')
cur = conn.cursor()
#Connect to database and Create Tables
def connect():
    #create owners table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Owner(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        DOB TEXT,
        Phone INTEGER,
        Address TEXT,
        Email TEXT,
        Password TEXT)""")
    
    #create emloyee table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Staff(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        DOB TEXT,
        Phone INTEGER,
        Address TEXT,
        Email TEXT,
        Password TEXT)""")

    #create customer table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Customer(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        DOB TEXT,
        Phone INTEGER,
        Address TEXT,
        Email TEXT,
        Password TEXT)""")

    #create products table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Product(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Price REAL,
        Isbn INTEGER,
        Address TEXT,
        Category TEXT)""")

    #create events table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Events(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Price Real,
        Isbn Integer,
        Address TEXT,
        Category TEXT)""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
        id INTEGER PRIMARY KEY,
        User_id INTEGER,
        Product_id INTEGER,
        FOREIGN KEY(User_id) REFERENCES Customer(id),
        FOREIGN KEY(Product_id) REFERENCES Product(id))""")

    conn.commit()
    conn.close()

########## Managing People ### Owner,Employee,Customer ##################
def insert(name,dob,phone,address,email,password,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    cur.execute(f"""
    INSERT INTO {db} VALUES(Null,?,?,?,?,?,?)""",(name,dob,phone,address,email,password))

    conn.commit()
    conn.close()

def view(db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {db}""")
    rows = cur.fetchall()
    conn.close()

    return rows

def search(name="",dob="",phone="",email="",address="",db=""):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {db}
        WHERE name = ? OR
              dob = ? OR
              phone = ? OR
              email = ? OR
              address = ? """,(name,dob,phone,email,address))
    rows = cur.fetchall()
    conn.close()

    return rows

def delete(id,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM {db} WHERE id = ? """,(id,)) 
    conn.commit()
    conn.close()

def update(id,name,dob,phone,address,email,password,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""UPDATE {db}
            SET name = ?, dob=?, phone=?,email=?,address=?,password=?
            WHERE id=?""",(name,dob,phone,address,email,password,id)) 
    conn.commit()
    conn.close()

################# Managing Products / Events DATA ########################
def insert_pd(name,price,isbn,address,category,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    if category == "Event":
        db = "Events"

    cur.execute(f"""
    INSERT INTO {db} VALUES(Null,?,?,?,?,?)""",(name,price,isbn,address,category))

    conn.commit()
    conn.close()

def view_pd(db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {db}""")
    rows = cur.fetchall()
    conn.close()

    return rows

def search_pd(name="",price="",isbn="",address="",category="",db=""):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {db}
        WHERE name = ? OR
              price = ? OR
              isbn = ? OR
              address = ? OR
              category = ? """,(name,price,isbn,address,category))
    rows = cur.fetchall()
    conn.close()

    return rows

def delete_pd(id,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM {db} WHERE id=?""",(id,)) 
    conn.commit()
    conn.close()

def update_pd(id,name,price,isbn,address,category,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""UPDATE {db}
            SET name = ?, price=?, isbn=?,address=?,category=?
            WHERE id=?""",(name,price,isbn,address,category,id)) 
    conn.commit()
    conn.close()

################### Managing Orders #################################
def create_order(userid,productid,db):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    cur.execute(f"""INSERT INTO {db}
        VALUES (NULL,?,?)""",(userid,productid))
    conn.commit()
    conn.close()

def search_order(userid):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT User_id,Name,Price,Address 
                    FROM Orders INNER JOIN Product
                    ON Orders.Product_id = Product.id
                    WHERE User_id = ?""",str(userid))
    rows = cur.fetchall()
    conn.close()

    return rows

def view_order(userid):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    cur.execute(f"""SELECT Name,Price 
                    FROM Orders INNER JOIN Product 
                    ON Orders.Product_id = Product.id
                    WHERE User_id = ?""",str(userid))
    
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    return rows

def view_all_orders():
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    cur.execute(f"""SELECT User_id,Name,Price 
                    FROM Orders INNER JOIN Product 
                    ON Orders.Product_id = Product.id""")
    
    rows = cur.fetchall()
    conn.close()

    return rows

    
connect()