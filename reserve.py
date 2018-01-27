#!/Python27/python

# This section imports modules for CGI handling
import cgi, cgitb, mysql.connector

# This section Creates instance of FieldStorage
form = cgi.FieldStorage()

# This section is for Getting data from html form
Py_room_id = form.getvalue('r_rid', 0)
Py_cust_id = form.getvalue('r_cid', 0)
Py_room_price = form.getvalue('r_price', 0)
Py_room_payment = form.getvalue('r_payment', '')
Py_room_datein = form.getvalue('r_datein', '')
Py_room_dateout = form.getvalue('r_dateout', '')
Py_room_type = form.getvalue('r_type', '')

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
sql = "INSERT INTO testing.room_reservation(rnum,cid,rprice,rpayment,date_in,date_out,type) VALUES('%s', '%s', '%s', '%s', '%s', '%s','%s')" %(Py_room_id, Py_cust_id, Py_room_price, Py_room_payment, Py_room_datein, Py_room_dateout,Py_room_type)

print "insert executed"

cursor.execute(sql)
db1.commit()    # Commit your changes in the database        
print "<body >"
print "<p>Record Updated. You added the following details to the table:</p>"
print "<br></br>"
print "<p4> Room id: %s </p4>" % Py_room_id
print "<br></br>"
print "<p5> Customer id: %s </p5>" % Py_cust_id
print "<br></br>"
print "<p6> Room Price: %s </p6>" % Py_room_price
print "<br></br>"
print "<p7> Room payment: %s </p7>" % Py_room_payment
print "<br></br>"
print "<p8> Room date in: %s </p8>" % Py_room_datein
print "<br></br>"
print "<p9> Room date out: %s </p9>" % Py_room_dateout
print "<br></br>"
print "<p10> Type of room: %s </p10>" % Py_room_type
print "<br></br>"
print "</body>"
db1.close()
  

  

