import os
import sys

def ArchivoNuevo():

    try:

        nombre = input("Ingrese el nombre del archivo que desea crear: ")

        with open(nombre+".txt", "w", encoding="utf-8")as archivo:
            texto = input("Ingrese texto a agregar: ")
            archivo.write(texto)

        print("Archivo creado con exito.")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

def LeerArchivo():
    nombre = input("Ingrese el nombre del archivo a leer: ")

    try:

        with open(nombre+".txt", "r", encoding="utf-8")as archivo:
            for lineas in archivo:
                print(lineas.strip())
            pos = archivo.tell()
            print('El archivo de texto tiene una longitud de {0} caracteres'.format(pos))

    except FileNotFoundError:
        print("Archivo inexistente.")

def AgregarTexto():

    nombre = input("Ingrese el nombre del archivo: ")

    try:

        with open(nombre+".txt", "a", encoding="utf-8")as archivo:
            texto = input("Ingrese texto a agregar: ")
            archivo.write(texto)

        print("Texto agregado con exito.")

    except IOError as e:
        print(f"Error al agregar contenido en el archivo: {e}")

def ReemplazarTexto():

    nombre = input("Ingrese el nombre del archivo: ")

    try:

        with open(nombre+".txt", "w", encoding="utf-8")as archivo:
            texto = input("Ingrese texto a agregar: ")
            archivo.write(texto)

        print("Texto reemplazado con exito.")

    except IOError as e:
        print(f"Error al reemplazar contenido en el archivo: {e}")

def EliminarArchivo():
    nombre = input("Ingrese nombre del archivo que quiera eliminar: ")
    texto = nombre + ".txt"
    try:
        os.remove(texto)
        print("Archivo eliminado con exito")
    except FileNotFoundError:
        print(f"El archivo {texto} no fue encontrado")
    except PermissionError:
        print(f"No tienes los permisos para eliminar el archivo {texto}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")    
while True:
    print("╔════════════════════════════════════════════╗")
    print("║               MENU PRINCIPAL.              ║")
    print("╠════════════════════════════════════════════╣")
    print("║ 1. Crear un archivo.  2. Leer un archivo.  ║")
    print("║ 3. Agregar texto.     4. Reemplazar texto. ║")
    print("║ 5. Eliminar           6. Salir             ║")
    print("╚════════════════════════════════════════════╝")

    opcion = input("Seleccione una opcion entre [1 - 5] -> ")

    if opcion == "1":
        ArchivoNuevo()
    elif opcion == "2":
        LeerArchivo()
    elif opcion == "3":
        AgregarTexto()
    elif opcion == "4":
        ReemplazarTexto()
    elif opcion == "5":
        EliminarArchivo()
    elif opcion == "6":
        sys.exit()    
    else:
        print("Opcion invalida.")