## funciones de validación


def validacionNum(x):
    """Función que valida que un ingreso sea de tipo numérico"""
    while True:
        if type(x) == int or type(x) == float:
            if x >= 0:
                break
            else:
                x = input("Este dato no permite valores negativos. Ingrese de nuevo: ")
                continue 
        else:
            try:
                x = float(x)
            except:
                x = input("El valor ingresado no es numérico. Ingrese de nuevo: ")
                continue
    return x

def validacionEnteros(x):
    """Función que valida que un ingreso sea un número entero"""
    while True:
        try:
            x = int(x)
            if x >= 0:
                break
            else:
                x = input("Este dato no permite valores negativos. Ingrese de nuevo: ")
                continue
            
        except ValueError:
            while True:
                try:
                    x = int(input("El valor ingresado no es aceptado, se debe ingresar un valor entero.\n Ingrese de nuevo: "))
                    break
                except:
                    continue
    return x

def rango1_a(x, a):
    """Función que valida que el numero ingresado se encuentre en el rango correcto"""
    while True:
        if x>=1 and x<=a:
            break
    
        else:
            try:
                x = int(input("El valor no se encuentra en el rango de opciones. Ingrese de nuevo la opción deseada: "))
                continue
            except:
                x = input("Valor no válido. Ingrese de nuevo: ")
                continue        
    return x

def validacionFlotantes(x):
    """Función que valida que un ingreso sea un número de punto flotante"""
    while True:
        try:
            x = float(x)
            break 
        except ValueError:
            while True:
                try:
                    x = float(input("El valor ingresado no es aceptado, se debe ingresar un valor de punto flotante o decimal.\n Ingrese de nuevo : "))
                    break
                except:
                    continue
    return x

def validacionCadenas(x):
    """Función que valida que un ingreso sea de tipo cadena de caracteres"""
    while True:
        if x.replace(' ', '').isalpha():
            break
        else:
            try:
                x = input("El valor ingresado no es una cadena de letras. Ingrese de nuevo: ")
            except:
                continue
    return x

     


## funciones CRUD

from main import client

# Funciones CRUD para la colección "equipos"
def crearEquipo(equipo):
    """"""
    client.equipos.insert_one(equipo)

def leerEquipo(serial):
    
    return client.equipos.find_one({'serial': serial})

def actualizarEquipo(serial, actualizacion):
    
    client.equipos.update_one({'serial': serial}, {'$set': actualizacion})

def borrarEquipo(serial):
    
    client.equipos.delete_one({'serial': serial})


# Funciones CRUD para la colección "responsables"
def crearResponsable(responsable):
    client.responsables.insert_one(responsable)

def leerResponsable(codigo):
    return client.responsables.find_one({'codigo': codigo})

def actualizarResponsable(codigo, updates):
    client.responsables.update_one({'codigo': codigo}, {'$set': updates})

def borrarResponsable(codigo):
    client.responsables.delete_one({'codigo': codigo})


# Funciones CRUD para la colección "ubicaciones"
def crearUbicacion(ubicacion):
    client.ubicaciones.insert_one(ubicacion)

def leerUbicacion(codigo):
    return client.ubicaciones.find_one({'codigo': codigo})

def actualizarUbicacion(codigo, updates):
    client.ubicaciones.update_one({'codigo': codigo}, {'$set': updates})

def borrarUbicacion(codigo):
    client.ubicaciones.delete_one({'codigo': codigo})
    