#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db.sqlite3')

print "Opened database successfully";

# cursor = conn.execute("SELECT emp_id, firstname, lastname from webapp_employees where firstname='Amit'")
cursor = conn.execute("SELECT MIN(emp_id),firstname,lastname from ( SELECT emp_id, firstname, lastname from webapp_employees ORDER BY emp_id DESC LIMIT 3 )")
for row in cursor:
   print "Employee_Id = ", row[0]
   print "FirstName = ", row[1]
   print "LastName = ", row[2]


print "Operation done successfully";
conn.close()