import sqlite3
import datetime

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

    #Table storing all the product details
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Product(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Price REAL,
        Isbn INTEGER,
        Address TEXT,
        Category TEXT)""")

    #Table storing all the event details
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Events(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Price Real,
        Isbn Integer,
        Address TEXT,
        Category TEXT)""")

    # Table storing all the Order details
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
        id INTEGER PRIMARY KEY,
        User_id INTEGER,
        Product_id INTEGER,
        FOREIGN KEY(User_id) REFERENCES Customer(id),
        FOREIGN KEY(Product_id) REFERENCES Product(id))""")

    #Table used as a backup, stores all completed orders
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Completed_Orders(
        id INTEGER PRIMARY KEY,
        Date_Completed TEXT,
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

def sort(db,factor):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {db} ORDER BY {factor} """)
    rows = cur.fetchall()
    conn.close()
    return rows

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

    cur.execute("""SELECT Name,Price 
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

    cur.execute(f"""SELECT Distinct Customer.id,Name,Address,Email
                    FROM Orders INNER JOIN Customer 
                    ON Orders.User_id = Customer.id""")
    
    rows = cur.fetchall()
    
    conn.commit()
    conn.close()

    return rows

def view_ordered_items(order_user_id):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    cur.execute("""SELECT Product.id,Name,Price,Isbn
                FROM Orders INNER JOIN Product
                ON Orders.Product_id = Product.id
                WHERE User_id = ?""",str(order_user_id))
    
    rows = cur.fetchall()
    
    conn.commit()
    conn.close()

    return rows

def transfer_orders(row):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    cur.execute(f""" INSERT INTO Completed_Orders (User_id,Product_id)
                    SELECT User_id,Product_id FROM Orders 
                    WHERE User_id = ?""",(row,))
    
    cur.execute(f""" DELETE FROM Orders
                 WHERE User_id = ?""",(row,))
    conn.commit()
    conn.close()
    #,{datetime.datetime.now()}

def get_invoice():
    pass
#insert('Sushil Bhandari','03/11/2003','073434434343','Cardiff','sushil','letmein','Owner')
connect()