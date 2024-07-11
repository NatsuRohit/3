import sqlite3
conn=sqlite3.connect('ecommerce.sqlite3')
cursor=conn.cursor()
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER,
        price INTEGER
                   )""")
    conn.commit()
create_table()
def insert(name,quantity,price):
    cursor.execute(
        """
        INSERT INTO products (name,quantity,price) VALUES(?,?,?)
        """,(name,quantity,price))
    conn.commit()
    print('Data inserted successfully')

name=input('Enter product name:-\t')
quantity=int(input('Enter the quantity:-\t'))
price=int(input('Enter the price:-\t'))
insert(name,quantity,price)

def getproduct():
    cursor.execute("""SELECT * FROM products""")
    print(cursor.fetchmany(5))
getproduct()