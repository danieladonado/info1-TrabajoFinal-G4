import pymongo

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
    return str(x)



## funciones CRUD

uri = "mongodb+srv://informatica1:bio123@cluster0.hj2pgzi.mongodb.net/?retryWrites=true&w=majority"

# Crear cliente que se conecte al servidor
client = pymongo.MongoClient(uri)


# Funciones CRUD para la colección "equipos"
def crearEquipo(equipo, datEquipos):
    """
    Inserta un diccionario con la información de un equipo
    en la colección de la base de datos
    
    Args:
        equipo (_type_): diccionario que representa un equipo
    """
    x = datEquipos.insert_one(equipo)


def leerEquipo(serial,datEquipos):
    """
    la función busca el parámetro en la colección y
    lo retorna si es encontrado

    Args:
        serial (_type_): numero de serie

    Returns:
        _type_: elemento buscado
    """
    if datEquipos.find_one({'serial': serial}) is None:
        print(f"No se encontró ningún equipo con el serial {serial}.")
    
    else:
        return client.equipos.find_one({'serial': serial})


def actualizarEquipo(serial, actualizacion):
    """La función actualiza un equipo guardado en la base de datos

    Args:
        serial (_type_): numero de serie del elemento en la base de datos
        actualizacion (_type_): elemento que reemplazará el anterior
    """
    client.equipos.update_one({'serial': serial}, {'$set': actualizacion})


def borrarEquipo(serial):
    """La función borra un equipo en la base de datos

    Args:
        serial (_type_): número de serie del equipo a borrar
    """
    client.equipos.delete_one({'serial': serial})


# Funciones CRUD para la colección "responsables"
def crearResponsable(responsable):
    """La función guarda un diccionario con un nuevo repsonsable
    en la base de datos

    Args:
        responsable (_type_): nuevo diccionario
    """
    client.responsables.insert_one(responsable)


def leerResponsable(codigo):
    """la función busca un código en la base de datos y
    muestra su información

    Args:
        codigo (_type_): codigo a buscar

    Returns:
        _type_: información del código buscado
    """
    if client.responsables.find_one({'codigo': codigo}) is None:
        print(f"No se encontró ningún responsable con el código {codigo}.")
    else:
        return client.responsables.find_one({'codigo': codigo})


def actualizarResponsable(codigo, updates):
    """La función actualiza un responsable en la base de datos

    Args:
        codigo (_type_): codigo del responsable
        updates (_type_): dato que reemplazará el anterior
    """
    client.responsables.update_one({'codigo': codigo}, {'$set': updates})


def borrarResponsable(codigo):
    """La función elimina un responsable de la base d edatos

    Args:
        codigo (_type_): codigo del responsable a eliminar
    """
    client.responsables.delete_one({'codigo': codigo})


# Funciones CRUD para la colección "ubicaciones"
def crearUbicacion(ubicacion):
    """La función añade una nueva ubicación a la colección indicada
    en la base de datos

    Args:
        ubicacion (_type_): diccionario con nueva ubicacion
    """
    client.ubicaciones.insert_one(ubicacion)


def leerUbicacion(codigo):
    """La función busca una ubicación en la base de datos

    Args:
        codigo (_type_): codigo de la ubicacion a buscar

    Returns:
        _type_: información de la ubicación encontrada
    """
    if client.ubicaciones.find_one({'codigo': codigo}) is None:
        print(f"No se encontró ningún equipo con el serial {codigo}.")
    
    else:
        return client.ubicaciones.find_one({'codigo': codigo})


def actualizarUbicacion(codigo, updates):
    """La función actualiza una ubicacion en la base de datos

    Args:
        codigo (_type_): codigo de la ubicacion en la base de datos
        updates (_type_): informacion que reemplazara la anterior
    """
    client.ubicaciones.update_one({'codigo': codigo}, {'$set': updates})


def borrarUbicacion(codigo):
    """La función elimina un responsable de la base d edatos

    Args:
        codigo (_type_): codigo del elemento a eliminar
    """
    client.ubicaciones.delete_one({'codigo': codigo})
    