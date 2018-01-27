

#!/Python27/python

# This section imports modules for CGI handling

from time import time, sleep

import cgi, cgitb 

# This section Creates instance of FieldStorage

# This section is for Getting data from html form


##This section connects to DATABASE

import mysql.connector


# Open database connection

GG_db1 = mysql.connector.connect(user='root', password='Sub@shini1993', host='localhost', database='inn')

 
# This section prepares a cursor object and gets sql query in sqlcmd variable

cursor = GG_db1.cursor()



tic1 = time()
sleep(0.05)
cursor.execute("""select customer.caddress from customer left join room_reservation on customer.cid = room_reservation.cid;""")
toc1 = time()
print toc1 - tic1



GG_db1.close()

