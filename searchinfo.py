#!C:/Python27/python.exe

import cgi, cgitb, mysql.connector

form = cgi.FieldStorage()
py_cid=form.getvalue('cid')
py_rtype=form.getvalue('type')
db1 = mysql.connector.connect(user='root', password='Sub@shini1993', host='localhost', database='testing')
cur = db1.cursor()
sql = "SELECT * FROM room_reservation WHERE cid='%s' and type='%s' " % (py_cid,py_rtype)
cur.execute(sql)


print "Content-type: text/html"
print
print "<html><head>"
print "<style>table, th, td{border:1px solid black;}</style>"
print "<style>"
print "<body {background-color: #D3D3D3;}>"
print "p1 {color: Red; font-size: 200%; text-align: center;}"
print "p2 {color: Blue; font-size: 100%; text-align: center;}"
print "p3 {color: Magenta; font-size: 100%; text-align: center;}"
print "</style>"
print "</head>"
print "<body {background-color: #D3D3D3;} >"
print "<h2>Output :  </h2>"
print "</body>"
print "<body>"
#print "<p3>You gave the following query: </br> %s</p3>" %query
#print "<br/>Using mysql.connector ...</br>"
#print "<br/><br/>"
#print "<p2> Output is given below: </p2>"
print "<table>"
print "<tr>"
#print cur.description
for i in range(len(cur.description)):
	print "<th>", cur.description[i][0],"</th>"
	#print "<br/>", cur.description[i][0]
print "</tr>"
for row in cur:
	print "<tr>"
	for j in range(len(cur.description)):
		print "<td>", row[j], "</td>"
	print "</tr>"

print "</table>"

print "</br>"

print "</body></html>"
db1.close()