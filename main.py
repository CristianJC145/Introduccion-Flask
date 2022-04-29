from validator import validate
from flask import Flask, render_template, request, redirect, url_for, flash
from models import productosModel

app = Flask(__name__)
app.secret_key = 'spbYO0JJOPUFLUikKYbKrpS5w3KUEnab5KcYDdYb'

@app.get("/")
def inicio():
   productos = productosModel.obtenerProductos()
   return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    #Recuperar los datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')

    response = validate(
    {   "nombre": nombre,
        "price": price
    }, 
    {   "nombre": "required|min:8",
        "price": "required|integer|min:8"
    },
    return_info=True
    )
    if response[0] == True:
        print(response) #[] ['El nombre es requerido', 'el precio debe ser un numero']
        productosModel.crearProducto(nombre=nombre, price=price)
    else:
        flash(response[2], 'error')
        return redirect(request.url)
    return redirect(url_for('inicio'))

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

@app.route('/eliminar/<string:id>')
def eliminar_producto(id):
        productosModel.eliminarProducto(id)
        return redirect(url_for('inicio'))

@app.route('/editar/<string:id>', methods=['GET','POST'])
def editar_producto(id):
    if request.method == 'GET':
        productos = productosModel.editarProducto(id)
        return render_template('editarProducto.html', producto = productos)

    price = request.form.get('price')
    nombre = request.form.get('nombre')

    try:
        productosModel.updateProductos(nombre, price,id)
    except:
        flash('No se ha podido editar el producto', 'error')
        return redirect(url_for('productos'))

    return redirect(url_for('inicio'))
    
# /edad/20  Naciste en el año 2000

app.run(debug=True)