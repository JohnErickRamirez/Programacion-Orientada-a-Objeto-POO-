import mysql.connector

class Articulos:
    def abrir (self):
        conexion = mysql.connector.connect(host="localhost", user="root", password="", database="bd1")
        return conexion
    def alta (self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"
        cursor.execute(sql, datos)  
        cone.commit()
        cone.close()

    def consultar (self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT descripcion, precio FROM articulos WHERE codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()
    

    def recuperar_todo(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()