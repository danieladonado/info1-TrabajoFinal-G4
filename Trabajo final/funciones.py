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


def imprimir_todos(coleccion):
    """FUNCIÓN GENERAL
    Función que imprime todos los elementos de la colección específica en la
    base de datos
    """
    # Obtener todos los documentos de la colección
    documentos = coleccion.find()
    
    # Imprimir la información de cada documento
    for documento in documentos:
        # Crear una lista con los valores de los campos del documento
        valores = [f"{clave}: {valor}" for clave, valor in documento.items()]
        # Unir los valores con comas y imprimirlos
        print(", ".join(valores))
        


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
                nuevo_valor = int(nuevo_valor)
                
            cambios[campo] = nuevo_valor
    
    # Actualizar el documento con los cambios
    coleccion.update_one({"numero de activo": numero_activo}, {"$set": cambios})
    
    print("Documento actualizado correctamente")


def borrarEquipo(numero_activo, coleccion):
    """La función elimina un equipo guardado en la base de datos 
    """
    # Buscar el documento por el número de activo
    documento = coleccion.find_one({"numero de activo": numero_activo})
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese número de activo")
        return
    # Eliminar el documento
    coleccion.delete_one({"numero de activo": numero_activo})
    print("Documento eliminado correctamente")


# Funciones CRUD para la colección "responsables"


def leerResponsable(codigo, coleccion):
    """la función busca un código en la base de datos y
    muestra su información
    """
    # Buscar el documento por el número de activo
    documento = coleccion.find_one({"codigo de responsable": codigo})
    
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese codigo de responsable")
        return
    
    # Imprimir la información del documento
    for campo, valor in documento.items():
        print(f"{campo}: {valor}")

def actualizarResponsable(codigo_responsable, coleccion):
    """La función actualiza un equipo guardado en la base de datos

    """
    # Buscar el documento por el código de responsable
    documento = coleccion.find_one({"codigo de responsable": codigo_responsable})
    
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese código de responsable")
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
            if campo == 'codigo de responsable':
                nuevo_valor = int(nuevo_valor)
                
            cambios[campo] = nuevo_valor
    
    # Actualizar el documento con los cambios
    coleccion.update_one({"codigo de responsable": codigo_responsable}, {"$set": cambios})
    
    print("Documento actualizado correctamente")

def borrarResponsable(codigo, coleccion):
    """La función elimina un responsable guardado en la base de datos 
    """
    # Buscar el documento por el codigo
    documento = coleccion.find_one({"codigo de responsable": codigo})
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese codigo")
        return
    # Eliminar el documento
    coleccion.delete_one({"codigo de responsable": codigo})
    print("Documento eliminado correctamente")


# Funciones CRUD para la colección "ubicaciones"


def leerUbicacion(codigo, coleccion):
    """la función busca un código en la base de datos y
    muestra su información
    """
    # Buscar el documento por el número de activo
    documento = coleccion.find_one({"codigo de ubicacion": codigo})
    
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese codigo de ubicacion")
        return
    
    # Imprimir la información del documento
    for campo, valor in documento.items():
        print(f"{campo}: {valor}")

def actualizarUbicacion(codigo_ubicacion, coleccion):
    """La función actualiza un equipo guardado en la base de datos

    """
    # Buscar el documento por el código de ubicacion
    documento = coleccion.find_one({"codigo de ubicacion": codigo_ubicacion})
    
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese código de ubicacion")
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
            if campo == 'codigo de responsable':
                nuevo_valor = int(nuevo_valor)
                
            cambios[campo] = nuevo_valor
    
    # Actualizar el documento con los cambios
    coleccion.update_one({"codigo de responsable": codigo_ubicacion}, {"$set": cambios})
    
    print("Documento actualizado correctamente")

def borrarUbicacion(codigo, coleccion):
    """La función elimina una ubicacion guardada en la base de datos 
    """
    # Buscar el documento por el codigo
    documento = coleccion.find_one({"codigo de ubicacion": codigo})
    # Verificar si se encontró algún documento
    if documento is None:
        print("No se encontró ningún documento con ese codigo")
        return
    # Eliminar el documento
    coleccion.delete_one({"codigo de ubicacion": codigo})
    print("Documento eliminado correctamente")
