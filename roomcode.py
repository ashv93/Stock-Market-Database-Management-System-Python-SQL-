#!/Python27/python

# This section imports modules for CGI handling
import cgi, cgitb, mysql.connector

# This section Creates instance of FieldStorage
form = cgi.FieldStorage()

# This section is for Getting data from html form
Py_room_type = form.getvalue('room_type', '')
Py_room_bed = form.getvalue('room_bed', 0)
Py_room_bed_type = form.getvalue('room_bedtype', '')
Py_smoke_preference = form.getvalue('smoke_preference', '')
Py_room_number = form.getvalue('room_number', 0)
Py_room_floor = form.getvalue('room_floor', 0)
Py_room_price = form.getvalue('room_price', 0)


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


#insert record in db   
sql = "INSERT INTO testing.room(rtype,rbed,rbedtype,rsmoke,rnum,rfloor,rprice) VALUES('%s','%s','%s','%s','%s','%s','%s')" %(Py_room_type,Py_room_bed,Py_room_bed_type,Py_smoke_preference,Py_room_number,Py_room_floor,Py_room_price)

cursor.execute(sql)
db1.commit()    # Commit your changes in the database        
print "<body >"
print "<p>Record Updated. You added the following details to the table:</p>"
print "<br></br>"
print "<p4> Room type: %s </p4>" % Py_room_type
print "<br></br>"
print "<p5> Room bed: %s </p5>" % Py_room_bed
print "<br></br>"
print "<p6> Room bed type: %s </p5>" % Py_room_bed_type
print "<br></br>"
print "<p7> Smoke preference: %s </p5>" % Py_smoke_preference
print "<br></br>"
print "<p8> Room number: %s </p5>" % Py_room_number
print "<br></br>"
print "<p9> Room floor number: %s </p5>" % Py_room_floor
print "<br></br>"
print "<p10> Room price: %s </p5>" % Py_room_price
print "<br></br>"
print "</body>"
db1.close()
  

  

