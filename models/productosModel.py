from config.database import db


def obtenerProductos():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("select * from productos")
    productos = cursor.fetchall() #Obtener todo
    #producto = cursor.fetchone() 
    
    cursor.close()
    return productos

def crearProducto(nombre,price):
    #Insertar los datos en la base de datos
    cursor = db.cursor()
    
    cursor.execute("insert into productos(nombre, price) values(%s, %s)", (
        nombre,
        price,
    ))
    cursor.close()