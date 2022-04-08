from wsgiref import validate
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

    response = Validate([
        {
            'value': nombre,
            'validators': 'required,min:8'
        },
        {
            'value': price,
            'validators': 'required,numeric'
        }
    ])
    print(response)

    is_valid = True

    if nombre == "":
        flash('El campo nombre es requerido', 'error')
        is_valid = False
        return redirect(request.url)
    if price =="":
        flash('El campo precio es requerido', 'error')
        is_valid == False
    if not price.isdigit():
        is_valid = False

    if not is_valid: 
        flash("No se ha creado el producto", "error")
        return render_template("crearProducto.html",
                nombre=nombre,
                price=price,
        )
    productosModel.crearProducto(nombre=nombre, price=price)
    return redirect(url_for('inicio'))

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

@app.route('/eliminar/<string:id>')
def eliminar_producto(id):
        cursor = db.cursor()
        cursor.execute("delete from productos where cod = %s", (id,))
        db.commit()
        return redirect(url_for('inicio'))

@app.route('/editar/<string:id>', methods=['GET','POST'])
def editar_producto(id):
    if request.method == 'GET':
        cursor = db.cursor()
        productos = cursor.execute("select * from productos where cod = %s", (id,))
        productos = cursor.fetchone()
        return render_template('editarProducto.html', producto = productos)

    price = request.form.get('price')
    nombre = request.form.get('nombre')

    try:
        cursor = db.cursor()
        cursor.execute("""update productos set nombre = %s,
            price = %s where cod = %s 
        """, (nombre, price, id,))

        db.commit()
    except:
        flash('No se ha podido editar el producto', 'error')
        return redirect(url_for('productos'))

    return redirect(url_for('inicio'))
    
# /edad/20  Naciste en el año 2000

app.run(debug=True)