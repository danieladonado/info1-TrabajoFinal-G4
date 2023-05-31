import pymongo

## funciones CRUD

uri = "mongodb+srv://informatica1:bio123@cluster0.hj2pgzi.mongodb.net/?retryWrites=true&w=majority"

# Crear cliente que se conecte al servidor
client = pymongo.MongoClient(uri)


def crear(dict, coleccion):
    """FUNCIÓN GENERAL
    Inserta un diccionario con la información 
    en la colección de la base de datos
    
    """
    x = coleccion.insert_one(dict)



# Funciones CRUD para la colección "equipos"


def leerEquipo(numero_activo, coleccion):
    """
    la función busca el parámetro en la colección y
    lo retorna si es encontrado
    """
    # Buscar el documento por el número de activo
    documento = coleccion.find_one({"numero de activo": numero_activo})
    
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese número de activo")
        return
    
    # Imprimir la información del documento
    for campo, valor in documento.items():
        print(f"{campo}: {valor}")



def actualizarEquipo(numero_activo, coleccion):
    """La función actualiza un equipo guardado en la base de datos

    """
    # Buscar el documento por el número de activo
    documento = coleccion.find_one({"numero de activo": numero_activo})
    
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese número de activo")
        return
    
    # Crear un diccionario para almacenar los cambios
    cambios = {}
    
    # Pedir al usuario que ingrese nuevos valores para cada campo
    for campo, valor in documento.items():
        # No actualizar el campo _id
        if campo == "_id":
            continue
        
        nuevo_valor = input(f"Ingrese un nuevo valor para el campo '{campo}' (valor actual: {valor}): ")

            
        # Si el usuario ingresó un valor, actualizar el campo
        if nuevo_valor != "":
            if campo == 'numero de activo':
                nuevo_valor == int(nuevo_valor)
                
            cambios[campo] = nuevo_valor
    
    # Actualizar el documento con los cambios
    coleccion.update_one({"numero de activo": numero_activo}, {"$set": cambios})
    
    print("Documento actualizado correctamente")


def borrarEquipo(serial):
    """La función borra un equipo en la base de datos

    Args:
        serial (_type_): número de serie del equipo a borrar
    """
    client.equipos.delete_one({'serial': serial})


# Funciones CRUD para la colección "responsables"


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
    