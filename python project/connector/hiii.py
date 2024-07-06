import mysql.connector as myConn
mydb=myConn.connect(host='loculhost',
                    username='root',
                    password='pratik@123',
                    database='codewithprateek')
print(mydb,"connection established.....")