#Probar la conexion y consular las tablas creadas
import mysql.connector

conexion=mysql.connector.connect(host="localhost", user="root", passwd="Styfler01", database="bd1") #,auth_plugin='mysql_native_password'
cursor=conexion.cursor()
#cursor.execute("show tables")
cursor.execute("SELECT * FROM articulos")
for tabla in cursor:
    print(tabla)
conexion.close()

def getRecords():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Styfler01", database="bd1")
        mycursor = mydb.cursor()
        print("Connected to MySQL")
    except mysql.connector.Error as err:
        print("Error: ", err)
   


    # python
    


    mydb.commit()
    print("commit")
    records = mycursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
        print("ID: ", row[0])
        print("Descripcion: ", row[1])
        print("Precio: ", row[2])
        print("\n")
    mycursor.close()
    print("valor de records: ", records)

# python
getRecords()

