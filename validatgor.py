import json
from validator import validate


"""
name = input("Nombre: ")
price = input("Precio: ")

response = validate(
    {   "name": name,
        "price": price
    }, 
    {   "name": "required|min:8",
        "price": "required|integer|min:8"
    },
    return_info=True
)

print(json.dumps(response[0]))"""

x = {
"Nombre":"Ricardo",
"Apellido":"Rodriguez",
"teléfono": 600000000,
"email":"ricardo@bodega.com",
"Segmento": ("AA"),
"N Compras":7,
"Productos comprados": [
{"Vino":"Vino tinto","Grados":14},
{"Vino":"Vino Blanco","Grados":11.5}
  ]
}

print(json.dumps(x))