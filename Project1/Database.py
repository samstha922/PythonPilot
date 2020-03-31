import pymysql
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
myCursor = connection.cursor() #needed to fire query of mysql
# myCursor.execute("""CREATE TABLE names
#     (
#     id int primary key,
#     name varchar(20)
#     )
#     """)

# myCursor.execute("""INSERT INTO names(id,name) VALUES(1,"Sam")
#
#     """)

# myCursor.execute("UPDATE name FROM names WHERE id = '1';")

# myCursor.execute("DELETE FROM names where id='1';")

myCursor.execute("SELECT * FROM names;")
print(myCursor.fetchall(), end="\n")
connection.commit()
connection.close()
