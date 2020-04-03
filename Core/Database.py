import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
myCursor = connection.cursor() #needed to fire query of mysql

# #----------- list the databases
# myCursor.execute("SHOW DATABASES")
# for x in myCursor:
#     print(x)

## ----------creates the table 'names' inside the database
# myCursor.execute("""CREATE TABLE names
#     (
#     id int primary key,
#     name varchar(20)
#     )
#     """)

# #--------alter the table
# myCursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

## ------inserts data into the table with given values
# myCursor.execute("""INSERT INTO names(id,name) VALUES(1,"Sam")
#
#     """)

# # -------- update the table with values
# myCursor.execute("UPDATE name FROM names WHERE id = '1';")

# #--------delete the data from table
# myCursor.execute("DELETE FROM names where id='1';")

# display the data
myCursor.execute("SELECT * FROM names;")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

connection.commit()
connection.close()

# #escaping the values - Escape query values by using the placholder %s method. Eg.sql = "SELECT * FROM customers WHERE address = %s" ;   adr = ("Yellow Garden 2", )
## Setting the offset from the 3rd item; mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

# # Inserting multiple data
# sql = """INSERT INTO names (id,name) VALUES (%s, %s)
#     """
# value = [
#     (2,'ram'),
#     (3,"shyam")
# ]
# myCursor.executemany(sql,value) #to execute many queries at once
# connection.commit()
# connection.close()
