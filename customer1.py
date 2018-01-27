#!/Python27/python

# This section imports modules for CGI handling
import cgi, cgitb, mysql.connector

# This section Creates instance of FieldStorage
form = cgi.FieldStorage()

# This section is for Getting data from html form
Py_cust_id = form.getvalue('c_cid', 0)
Py_cust_name = form.getvalue('c_cname', '')
Py_cust_type = form.getvalue('c_ctype', )
Py_cust_age = form.getvalue('c_cage', 0)
Py_cust_crtype = form.getvalue('c_crtype', '')
Py_cust_address = form.getvalue('c_caddress', '')


#pay heading and layout
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print("""
<body style="background-color:lightgrey;">
<h1 style="text-align:center"> RESULTS </h1>
""")


##This section creates DATABASE
import mysql.connector
# Open database connection
db1 = mysql.connector.connect(user='root', password='Sub@shini1993', host='localhost', database='testing')
# This section prepares a cursor object
cursor = db1.cursor() 
#This section creates DATABASE
import  mysql.connector
# Open database connection
db1 = mysql.connector.connect(user='root', password='Sub@shini1993', host='localhost', database='testing')
#This section prepares a cursor object
cursor = db1.cursor()

#compute ne employee id from existing emp ids   
sq="""USE testing;"""
cursor.execute(sq)
print "db is opened"


#insert record in db   
sql = "INSERT INTO testing.customer(cid,cname,ctype,cage,crtype,caddress) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" %(Py_cust_id, Py_cust_name, Py_cust_type, Py_cust_age, Py_cust_crtype, Py_cust_address )

print "insert executed"

cursor.execute(sql)
db1.commit()    # Commit your changes in the database        
print "<body >"
print "<p>Record Updated. You added the following details to the table:</p>"
print "<br></br>"
print "<p4> Customer ID: %s </p4>" % Py_cust_id
print "<br></br>"
print "<p5> Customer name: %s </p5>" % Py_cust_name
print "<br></br>"
print "<p6> Customer Type: %s </p4>" % Py_cust_type
print "<br></br>"
print "<p7> Customer age: %s </p5>" % Py_cust_age
print "<br></br>"
print "<p8> Customer preference type: %s </p4>" % Py_cust_crtype
print "<br></br>"
print "<p9> Customer address: %s </p5>" % Py_cust_address
print "<br></br>"
print "</body>"
db1.close()
  

  

