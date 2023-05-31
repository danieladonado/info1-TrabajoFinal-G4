"""Integrantes:

-Laura Acevedo González
-Diego Alejandro Jaramillo Arroyave

"""
import csv
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


db = client.test
mydb = client["informatica1"]
datEquipos = mydb["equiposData"]
datRespon = mydb["responsablesData"]
datRespon = mydb["ubicacionesData"]

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

while True:

    
 
    menu = input(
    "\033[1;3;96m \nBienvenido al menú principal \033[0m\n\n 1. Menú de equipos.\n 2. Menú de responsables.\n 3. Menú de ubicaciones.\n 4. Salir.\n\nIngrese una opción: "
    )
    menu = validacionEnteros(menu)
    menu = rango1_a(menu,4)

    if menu == 1:
        """ 
        Sección del menú para la colección de equipos 
        """
        while True:
            equipo = input(
            "\n\nMenú de equipos\n\n 1. Ingresar equipo de forma manual.\n 2. Ingresar equipo de forma automática.\n 3. Actualizar equipo.\n 4. Buscar equipo.\n 5. Ver todos los equipos.\n 6. Eliminar equipo.\n 7. Volver al menú principal.\n\nIngrese una opción: "
            )
            equipo = validacionEnteros(equipo)
            equipo = rango1_a(equipo,7)

            if equipo == 1:
                """ 
                Sección de adición de un nuevo equipo a la base de datos
                """
                serialN = input("\nIngrese el número de serial: ")
                serialN = validacionEnteros(serialN)
                
                activoN = input("\nIngrese el número de activo: ")
                activoN =validacionEnteros(activoN)

                nombreN = input("\nIngrese el nombre del equipo: ")
                nombreN = validacionCadenas(nombreN)

                marcaN = input("\nIngrese la marca del equipo: ")
                marcaN = validacionCadenas(marcaN)

                codeUbi = input("\nIngrese el código de ubicación: ")
                codeUbi =validacionEnteros(codeUbi)

                coderesp = input("\nIngrese el código de responsable: ")
                coderesp = validacionEnteros(coderesp)

                insertar={'serial':serialN,
                                'numero de activo':activoN,
                                'nombre':nombreN,
                                'marca':marcaN,
                                'codigo de ubicacion':codeUbi,
                                'codigo de responsable':coderesp,
                                }
                
                crearEquipo(insertar,datEquipos)
                print("\nEquipo guardado adecuadamente\n")
                             
            if equipo == 2:
                """Sección de adición de equipo de forma automática
                """
                confirmar = input("Ingrese '1' para confirmar el ingreso de información automática desde el archivo, o '2' para regresar al menú: ")
                confirmar = validacionEnteros(confirmar)
                confirmar = rango1_a(confirmar,2)
                
                if confirmar == 1:
                    with open("inventarioIPS.csv", newline="", encoding="utf-8") as csvfile:
                        reader = csv.reader(csvfile, delimiter=";")
                        # Obtener los nombres de las columnas de la primera fila
                        header = next(reader)
                        # Obtener los índices de las columnas específicas
                        name_index = header.index("NOMBRE")
                        marca_index = header.index("MARCA")
                        ubicacion_index = header.index("SEDE")
                        serial_index = header.index("SERIE")
                        
                        for row in reader:
                            # Acceder a los datos de columnas específicas utilizando los índices
                            name = row[name_index]
                            brand = row[marca_index]
                            location = row[ubicacion_index]
                            
                            # Hacer algo con los datos extraídos
                            
                            #generar números aleatorios
                            import random
                            for i in range(3):
                                num_digits = 5
                                digits = [str(random.randint(0, 9)) for _ in range(num_digits)]
                                random_number = int(''.join(digits))

                            
                            print(f"Nombre: {name}, Marca: {brand}, Sede: {location}")
                    
                elif confirmar ==2:
                    continue
                
            if equipo == 3:
                pass
            if equipo == 4:
                pass
            if equipo == 5:
                pass
            if equipo == 6:
                pass
            if equipo == 7:
                pass

            break

    if menu == 2:
        pass
    if menu == 3:
        pass
    if menu == 4:
        print("\n\nPrograma finalizado exitosamente.")
        break
