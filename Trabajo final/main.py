"""Integrantes:

-Laura Acevedo González
-Diego Alejandro Jaramillo Arroyave

"""
import csv
from validaciones import validacionNum
from validaciones import validacionEnteros
from validaciones import rango1_a
from validaciones import validacionFlotantes
from validaciones import validacionCadenas
from validaciones import validacionCadenas1

from funciones import crear
from funciones import leerEquipo
from funciones import actualizarEquipo
from funciones import borrarEquipo
from funciones import leerResponsable
from funciones import actualizarResponsable
from funciones import borrarResponsable
from funciones import imprimir_todos
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
datUbi = mydb["ubicacionesData"]

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Inicio código aplicación CRUD

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
                serialN = validacionCadenas1(serialN)
                
                activoN = input("\nIngrese el número de activo: ")
                activoN =validacionEnteros(activoN)

                nombreN = input("\nIngrese el nombre del equipo: ")
                nombreN = validacionCadenas(nombreN)

                marcaN = input("\nIngrese la marca del equipo: ")
                marcaN = validacionCadenas1(marcaN)

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
                
                crear(insertar,datEquipos)
                print("\nEquipo guardado adecuadamente\n")
                continue
                             
            if equipo == 2:
                """Sección de adición de equipo de forma automática
                """
                confirmar = input("Ingrese '1' para confirmar el ingreso de información automática desde el archivo, o '2' para regresar al menú: ")
                confirmar = validacionEnteros(confirmar)
                confirmar = rango1_a(confirmar,2)
                
                if confirmar == 1:
                    with open("Trabajo final\inventarioIPS.csv", newline="", encoding="utf-8") as csvfile:
                        reader = csv.reader(csvfile, delimiter=";")
                        # Obtener los nombres de las columnas de la primera fila
                        header = next(reader)
                        # Obtener los índices de las columnas específicas
                        name_index = header.index("NOMBRE")
                        marca_index = header.index("MARCA")
                        serial_index = header.index("SERIE")
                        
                        for row in reader:
                            # Acceder a los datos de columnas específicas utilizando los índices
                            name = row[name_index]
                            brand = row[marca_index]
                            serial = row[serial_index]
                            
                            # Hacer algo con los datos extraídos
                            
                            #generar números aleatorios
                            import random

                            num_digits = 5
                            digits1 = [str(random.randint(0, 9)) for _ in range(num_digits)]
                            random_number1 = int(''.join(digits1))
                            #
                            digits2 = [str(random.randint(0, 9)) for _ in range(num_digits)]
                            random_number2 = int(''.join(digits2))
                            #
                            digits3 = [str(random.randint(0, 9)) for _ in range(num_digits)]
                            random_number3 = int(''.join(digits3))
                            
                            insertar = {'serial':serial,
                                'numero de activo':random_number1,
                                'nombre':name,
                                'marca':brand,
                                'codigo de ubicacion':random_number2,
                                'codigo de responsable':random_number3,
                                }
                
                            crear(insertar,datEquipos)
                            print("Ingreso automático exitoso.")
                            continue
                    
                elif confirmar ==2:
                    continue
                
            if equipo == 3:
                """Sección para actualizar información guardada
                """
                numeroAc = input("Ingrese el número de activo a buscar: ")
                numeroAc = validacionEnteros(numeroAc)
                
                actualizarEquipo(numeroAc,datEquipos)
                print() 
                continue  
                    
            if equipo == 4:
                """Sección para buscar información de un equipo
                """
                numeroAc = input("Ingrese el número de activo a buscar: ")
                numeroAc = validacionEnteros(numeroAc)
                print()
                
                leerEquipo(numeroAc,datEquipos)
                continue
                
            if equipo == 5:
                print("\nLos equipos registrados son: \n\n")
                imprimir_todos(datEquipos)
                print()
                continue
                
            if equipo == 6:
                """Sección para eliminar información de un equipo
                """
                numeroAc = input("Ingrese el número de activo a eliminar: ")
                numeroAc = validacionEnteros(numeroAc)
                print()
                borrarEquipo(numeroAc,datEquipos)
                continue   
                
            if equipo == 7:
                pass

            break

    if menu == 2:
        while True:
            responsable = input(
            "\n\nMenú de responsables\n\n 1. Ingresar responsable.\n 2. Actualizar responsable.\n 3. Buscar responsable.\n 4. Ver todos los responsables.\n 5. Eliminar responsable.\n 6. Volver al menú principal.\n\nIngrese una opción: "
            )
            responsable = validacionEnteros(responsable)
            responsable = rango1_a(responsable, 6)

            if responsable == 1:
                """ 
                Sección de adición de un nuevo responsable a la base de datos
                """
                coderesp = input("\nIngrese el código de responsable: ")
                coderesp = validacionEnteros(coderesp)

                nom = input("Ingrese el nombre del responsable: ")
                nom = validacionCadenas(nom)

                prenom = input("Ingrese el apellido del responsable: ")
                prenom = validacionCadenas(prenom)

                id = input("Ingrese la identificación del responsable: ")
                id = validacionEnteros(id)

                cargo = input("Ingrese el cargo del responsable: ")
                cargo = validacionCadenas(cargo)

                insertar = {'codigo de responsable':coderesp,
                                'nombre':nom,
                                'apellido':prenom,
                                'id':id,
                                'cargo':cargo,
                                }
                
                crear(insertar,datRespon)
                print("\nResponsable guardado adecuadamente\n")
                continue
            
            if responsable == 2:
                """Sección para actualizar información guardada
                """
                code = input("Ingrese el codigo de responsable a buscar: ")
                code = validacionEnteros(code)
                
                actualizarResponsable(code,datRespon)
                print() 
                continue  
            
            if responsable == 3:
                """Sección para buscar información de un responsable
                """
                code = input("Ingrese el codigo de responsable a buscar: ")
                code = validacionEnteros(code)
                print()
                
                leerResponsable(code,datRespon)
                continue
            
            if responsable == 4:
                print("\nLos responsables registrados son: \n\n")
                imprimir_todos(datRespon)
                print()
                continue
        
            if responsable == 5:
                """Sección para eliminar información de un responsable
                """
                codigo = input("Ingrese el codigo de responsable a eliminar: ")
                codigo = validacionEnteros(codigo)
                print()
                borrarResponsable(codigo,datRespon)
                continue
                
            if responsable == 6:
                break
        
    if menu == 3:
        while True:
            ubicacion = input(
            "\n\nMenú de ubicación\n\n 1. Ingresar ubicación.\n 2. Actualizar ubicación.\n 3. Buscar ubicación.\n 4. Ver todas las ubicaciones.\n 5. Eliminar ubicación.\n 6. Volver al menú principal.\n\nIngrese una opción: "
            )
            ubicacion = validacionEnteros(ubicacion)
            ubicacion = rango1_a(ubicacion, 6)

            if ubicacion == 1:
                """ 
                Sección de adición de un nueva ubicación a la base de datos
                """
                codeUbi = input("\nIngrese el código de ubicación: ")
                codeUbi = validacionEnteros(codeUbi)

                nomUbi = input("Ingrese el nombre de la ubicación: ")
                nomUbi = validacionCadenas1(nomUbi)

                piso = input("Ingrese el número de piso: ")
                piso = validacionEnteros(piso)

                telefono = input("Ingrese el teléfono del responsable: ")
                telefono = validacionEnteros(telefono)

                insertar = {'codigo de ubicacion':codeUbi,
                                'nombre':nomUbi,
                                'piso':piso,
                                'telefono':telefono,
                                }
                
                crear(insertar,datUbi)
                print("\nUbicación guardada adecuadamente\n")
                continue
            
            if ubicacion == 2:
                """Sección para actualizar información guardada
                """
                code = input("Ingrese el codigo de ubicacion a buscar: ")
                code = validacionEnteros(code)
                
                actualizarUbicacion(code,datUbi)
                print() 
                continue  
            
            if ubicacion == 3:
                """Sección para buscar información 
                """
                code = input("Ingrese el codigo de ubicacion a buscar: ")
                code = validacionEnteros(code)
                print()
                
                leerUbicacion(code,datUbi)
                continue
            
            if ubicacion == 4:
                print("\nLas ubicaciones registradas son: \n\n")
                imprimir_todos(datUbi)
                print()
                continue
            
            if ubicacion == 5:
                """Sección para eliminar información de un responsable
                """
                codigo = input("Ingrese el codigo de ubicacion a eliminar: ")
                codigo = validacionEnteros(codigo)
                print()
                borrarUbicacion(codigo,datUbi)
                continue
            
            if ubicacion == 6:
                pass

            break
        
    if menu == 4:
        print("\n\nPrograma finalizado exitosamente.")
        break
