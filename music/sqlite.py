import random
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()


def create_table():
    c.execute('create table if not exists email (id, email)')


def dynamic_data():
    emailid= random.random()#range(0,100)
    email= 'amitjha3'
    c.execute("insert into email (id, email) values (?,?)",(emailid,email))
    conn.commit()


create_table()
# dynamic_data()
for i in range(5):
    dynamic_data()
c.close()
conn.close()

#fetching rows from db
# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# c.execute("SELECT * from email where email='amijha'")
# print c.fetchone()  #for fetching one row from table
# # for row in c:
# #     print row # will be a list


# try:
#     #SQL Code
# except sqlite3.Error as e:
#         print "An error occurred:", e.args[0]