"""integrantes:

-Laura Acevedo González
-Diego Alejandro Jaramillo Arroyave

"""

from funciones import validacionNum
from funciones import validacionEnteros
from funciones import rango1_a
from funciones import validacionFlotantes
from funciones import validacionCadenas

from funciones import crearEquipo
from funciones import leerEquipo
from funciones import actualizarEquipo
from funciones import borrarEquipo
from funciones import crearResponsable
from funciones import leerResponsable
from funciones import actualizarResponsable
from funciones import borrarResponsable
from funciones import crearUbicacion
from funciones import leerUbicacion
from funciones import actualizarUbicacion
from funciones import borrarUbicacion

### Conexión con la base de datos llamada informatica1
import pymongo

uri = "mongodb+srv://informatica1:bio123@cluster0.hj2pgzi.mongodb.net/?retryWrites=true&w=majority"

# Crear cliente que se conecte al servidor
client = pymongo.MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

