- Jose Velazque
- Jesus Vazquez
- Bermys Santana

## Tipos de Archivos

#### Definición general:
Los archivos son secuencias de bytes almacenadas en un dispositivo de almacenamiento (como un disco duro o SSD). La forma en que estos bytes se interpretan determina el "tipo" de archivo.

- Archivos de Texto:

Contienen secuencias de caracteres legibles por humanos (letras, números, símbolos) codificados según un estándar (como ASCII, UTF-8, etc.). Pueden abrirse y leerse directamente con un editor de texto simple.

Ejemplos:  .txt, .py, .html, .css, .csv, .json, .xml. (Aunque CSV y JSON tienen estructura, su contenido son caracteres legibles).

- Archivos Binarios:

Contienen datos en formato binario que no están destinados a ser interpretados como caracteres de texto. Su contenido solo tiene sentido para el programa que sabe cómo leer su estructura interna. No pueden leerse directamente con un editor de texto simple (aparecerían como caracteres sin sentido o símbolos extraños).

Ejemplos: Imágenes (.jpg, .png), videos (.mp4), archivos ejecutables (.exe), documentos de Word (.docx), archivos comprimidos (.zip, .rar).

- Archivos CSV (Comma Separated Values - Valores Separados por Comas):

Un tipo específico de archivo de *texto* utilizado para almacenar datos tabulares (en forma de tabla). Cada línea del archivo representa una fila de la tabla, y los valores dentro de cada fila están separados por un delimitador (comúnmente una coma, pero puede ser punto y coma, tabulación, etc.). Son muy utilizados para intercambiar datos entre hojas de cálculo y bases de datos. Ejemplo (contenido):

Nombre,Edad,Ciudad
Alice,30,Madrid
Bob,25,Barcelona

- Archivos JSON (JavaScript Object Notation - Notación de Objetos de JavaScript):

Un tipo específico de archivo de *texto* ligero y fácil de leer/escribir para humanos, y fácil de parsear/generar para máquinas. Es un formato común para el intercambio de datos, especialmente en aplicaciones web. Representa datos como pares clave-valor (objetos/diccionarios) y listas (arrays). Ejemplo (contenido):

{
  "nombre": "Alice",
  "edad": 30,
  "ciudades": ["Madrid", "Barcelona"]
}

## Apertura y cierre de archivos.

Para interactuar con un archivo (leer, escribir, etc.), primero debes "abrirlo". Esto crea un objeto archivo en la memoria que representa la conexión al archivo físico y permite realizar operaciones sobre él. Una vez que terminas de trabajar con el archivo, debes "cerrarlo" para liberar los recursos del sistema asociados y asegurar que los datos escritos se guarden correctamente.

- Función open(): Es la función principal en Python para abrir archivos.

Sintaxis básica: open(nombre_archivo, modo)

nombre_archivo: Una cadena con la ruta al archivo (puede ser relativa o absoluta).

modo: Una cadena que especifica cómo se abrirá el archivo (ver modos de escritura/lectura más adelante). Los modos comunes son 'r' (lectura), 'w' (escritura, sobrescribe), 'a' (añadir). Por defecto, es 'r' (lectura en modo texto). Puedes añadir 't' (texto) o 'b' (binario) para especificar el modo de contenido, aunque 't' es el predeterminado para 'r', 'w', 'a'.

Ejemplo:  archivo = open('mi_documento.txt', 'r')

- Método close(): Es un método del objeto archivo que cierra la conexión al archivo.
Sintaxis: objeto_archivo.close()

Ejemplo: archivo.close()
Importancia: Cerrar el archivo es crucial para garantizar que todos los datos escritos se guarden en el disco y para liberar los bloqueos que el sistema operativo pueda haber puesto sobre el archivo. Olvidar cerrar archivos, especialmente en programas largos, puede llevar a pérdida de datos o problemas de recursos.

### Lectura de archivos: métodos read(), readline(), y readlines().

Estos son métodos del objeto archivo (obtenido al abrir un archivo en modo lectura, 'r') que permiten extraer datos del archivo de diferentes maneras.

- Método read(size=-1): Lee el contenido completo del archivo como una única cadena de texto (si se abre en modo texto) o como un objeto bytes (si se abre en modo binario). Si se especifica el argumento size, lee hasta size caracteres/bytes.

Retorno: Una cadena de texto o bytes con el contenido leído. Si se alcanza el final del archivo, devuelve una cadena/bytes vacíos ('' o b'').

Ejemplo:
    with open('archivo.txt', 'r') as f:
    contenido_completo = f.read()
    print(contenido_completo)


- Método readline(): Lee una única línea del archivo, incluyendo el carácter de nueva línea (\n) si está presente al final de la línea.

Retorno: Una cadena de texto con la línea leída. Si se alcanza el final del archivo, devuelve una cadena vacía ('').

Ejemplo:
    with open('archivo.txt', 'r') as f:
    primera_linea = f.readline()
    segunda_linea = f.readline()
    print("Primera:", primera_linea)
    print("Segunda:", segunda_linea)

- Método readlines(): Lee todas las líneas del archivo y las devuelve como una lista de cadenas, donde cada cadena es una línea del archivo (incluyendo los caracteres de nueva línea).

Retorno: Una lista de cadenas.

Ejemplo:
    with open('archivo.txt', 'r') as f:
    lista_lineas = f.readlines()
    print(lista_lineas)

Los objetos archivo abiertos en modo texto son iterables línea por línea, lo cual es a menudo más eficiente para archivos grandes que readlines().

Ejemplo:
    with open('archivo.txt', 'r') as f:
    for linea in f:
    print(linea, end='') # end='' evita doble salto de línea si la línea ya tiene \n

## Escritura de archivos: modos w, a, r+.

Estos son modos que se pasan a la función open() para especificar cómo se comportará la operación de escritura.

- Modo 'w' (write - escritura):
       Abre un archivo para escritura. Si el archivo existe, su contenido es truncado (borrado) antes de abrirlo y Si el archivo no existe, se crea un nuevo archivo.
Precaución: Usar 'w' elimina el contenido existente si el archivo ya existe.

Ejemplo:
    with open('nuevo_archivo.txt', 'w') as f:
    f.write("Esta es la primera línea.\n")
    f.write("Esta es la segunda línea.")
#Si 'nuevo_archivo.txt' existía, su contenido anterior se perdió.

- Modo 'a' (append - añadir):
        Abre un archivo para escritura. Si el archivo existe, los nuevos datos se añaden al final del contenido existente y si el archivo no existe, se crea un nuevo archivo.
       
Ejemplo:
    with open('registro.log', 'a') as f:
    f.write("Entrada de log 1.\n")
Si ejecutas este código de nuevo, añadirá "Entrada de log 1.\n" al final del archivo.

- Modo 'r+' (read and write - lectura y escritura):
       Abre un archivo para ambas operaciones: lectura y escritura. El archivo debe existir. Si no existe, se produce un error (FileNotFoundError).

El puntero de lectura/escritura se posiciona al principio del archivo. La escritura en este modo sobrescribe el contenido existente a partir de la posición actual del puntero.
    
Ejemplo: 
#Asume que 'mi_documento.txt' ya existe con contenido
with open('mi_documento.txt', 'r+') as f:
    contenido_original = f.read() # Lee todo el contenido
    print("Contenido original:", contenido_original)

    f.seek(0) # Vuelve al principio del archivo
    f.write("NUEVO ") # Sobrescribe los primeros 6 caracteres
    f.truncate() # Elimina el resto del contenido después de la posición actual (opcional, si quieres reemplazar completamente)

#El archivo ahora podría empezar con "NUEVO " seguido del resto del contenido original si no se usó truncate, o solo "NUEVO " si se usó truncate después de la escritura.

 Existen otros modos combinados como 'w+' (escritura y lectura, trunca el archivo si existe) y 'a+' (añadir y lectura, el puntero de lectura está al principio, pero la escritura siempre es al final).


*   El archivo debe existir. Si no existe, se produce un error (FileNotFoundError).
        *   El puntero de lectura/escritura se posiciona al principio del archivo.
        *   La escritura en este modo sobrescribe el contenido existente a partir de la posición actual del puntero.
    *   Ejemplo:

#Asume que 'mi_documento.txt' ya existe con contenido
with open('mi_documento.txt', 'r+') as f:
    contenido_original = f.read() # Lee todo el contenido
    print("Contenido original:", contenido_original)

    f.seek(0) # Vuelve al principio del archivo
    f.write("NUEVO ") # Sobrescribe los primeros 6 caracteres
    f.truncate() # Elimina el resto del contenido después de la posición actual (opcional, si quieres reemplazar completamente)

#El archivo ahora podría empezar con "NUEVO " seguido del resto del contenido original si no se usó truncate, o solo "NUEVO " si se usó truncate después de la escritura.


    *   Notas: Existen otros modos combinados como 'w+' (escritura y lectura, trunca el archivo si existe) y 'a+' (añadir y lectura, el puntero de lectura está al principio, pero la escritura siempre es al final).

---

## Uso de bloques try y except para manejo de excepciones.

•   Definición: Las operaciones con archivos pueden fallar por diversas razones (el archivo no existe, no tienes permisos para leer/escribir, el disco está lleno, etc.). Estas situaciones generan "excepciones". Los bloques try...except son la forma estándar en Python de "atrapar" o "capturar" estas excepciones y manejar el error de forma controlada, evitando que el programa termine abruptamente.

•   Estructura:

try:
    # Código que podría generar una excepción (ej: abrir un archivo)
    operacion_riesgosa()
except TipoDeExcepcion:
    # Código que se ejecuta si ocurre esa excepción
    manejar_el_error()
except OtroTipoDeExcepcion as e:
    # Puedes capturar la excepción en una variable 'e' para obtener detalles
    print(f"Ocurrió un error: {e}")
    manejar_el_error_diferente()
except:
    # Bloque general para cualquier otra excepción (menos específico, usar con precaución)
    print("Ocurrió un error desconocido")
else:
    # (Opcional) Código que se ejecuta si el bloque try se completa SIN excepciones
    print("La operación fue exitosa")
finally:
    # (Opcional) Código que SIEMPRE se ejecuta, ocurra o no una excepción
    # Útil para limpieza de recursos (aunque 'with' es mejor para archivos)
    print("Este bloque siempre se ejecuta")


##   Excepciones comunes en archivos:
    *   FileNotFoundError: El archivo o directorio no existe.
    *   PermissionError: No tienes los permisos necesarios para acceder al archivo.
    *   IsADirectoryError: Intentaste abrir un directorio como si fuera un archivo.
    *   IOError: Un error general de entrada/salida (puede englobar las anteriores o ser por otros motivos).

•   Ejemplo con archivos:

nombre_archivo = 'archivo_que_no_existe.txt'
try:
    with open(nombre_archivo, 'r') as f:
        contenido = f.read()
        print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
except PermissionError:
    print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
except Exception as e: # Captura cualquier otra excepción I/O
    print(f"Ocurrió un error inesperado al leer el archivo: {e}")

print("El programa continúa después del manejo de error.")


---

## Comprobación de la existencia de archivos.

•   Definición: A veces, antes de intentar abrir un archivo para leer o realizar una operación que depende de su existencia, puedes querer verificar si el archivo o directorio existe en el sistema de archivos.

•   Biblioteca os: El módulo os (Operating System) proporciona funciones para interactuar con el sistema operativo, incluyendo la manipulación de rutas de archivos.

•   Función os.path.exists(path):
    *   Definición: Devuelve True si path se refiere a una ruta existente (archivo o directorio). Devuelve False en caso contrario.
    *   Ejemplo:

import os

nombre_archivo = 'mi_documento.txt'
if os.path.exists(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' existe.")
    # Ahora es seguro intentar abrirlo
    try:
        with open(nombre_archivo, 'r') as f:
            contenido = f.read()
            print("Contenido:", contenido)
    except PermissionError:
         print("Pero no tienes permisos para leerlo.")
else:
    print(f"El archivo '{nombre_archivo}' NO existe.")
    # Puedes decidir crearlo, notificar al usuario, etc.


•   Nota: Para operaciones de lectura, a menudo se prefiere usar try...except FileNotFoundError directamente, ya que es más "pythónico" (pedir perdón en lugar de pedir permiso - EAFP: Easier to Ask for Forgiveness than Permission). Sin embargo, os.path.exists() es útil para lógica condicional más compleja (ej: "si el archivo de configuración existe, úsalo; si no, usa valores por defecto").

---

## Lectura y escritura usando la biblioteca csv.

•   Definición: La biblioteca estándar de Python csv proporciona clases y funciones para trabajar fácilmente con archivos CSV, manejando automáticamente detalles como comillas dentro de los campos, diferentes delimitadores y saltos de línea.

•   Lectura (csv.reader):
    *   Definición: Crea un objeto lector que itera sobre las líneas del archivo CSV, donde cada línea es interpretada como una lista de cadenas (los campos).
    *   Uso:

import csv

with open('datos.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
    # newline='' es crucial para evitar problemas con saltos de línea
    # encoding='utf-8' es recomendado para manejo de caracteres especiales
    lector_csv = csv.reader(archivo_csv)

    # Opcional: saltar la fila de encabezado
    # next(lector_csv)

    print("Datos leídos:")
    for fila in lector_csv:
        # 'fila' es una lista de strings
        print(fila)
        # Acceder a campos individuales: fila[0], fila[1], etc.


•   Escritura (csv.writer):
    *   Definición: Crea un objeto escritor que permite escribir datos (típicamente listas o tuplas) en formato CSV en un archivo.
    *   Uso:

import csv

datos_para_escribir = [
    ['Nombre', 'Edad', 'Ciudad'], # Encabezado
    ['Alice', '30', 'Madrid'],
    ['Bob', '25', 'Barcelona'],
    ['Charlie', '22', 'Sevilla, España'] # Ejemplo con coma en un campo
]

with open('salida.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    # newline='' es crucial para evitar saltos de línea adicionales
    # encoding='utf-8' es recomendado
    escritor_csv = csv.writer(archivo_csv)

    # Escribir varias filas a la vez
    escritor_csv.writerows(datos_para_escribir)

    # O escribir fila por fila
    # for fila in datos_para_escribir:
    #     escritor_csv.writerow(fila)

print("Archivo 'salida.csv' creado.")


•   csv.DictReader y csv.DictWriter: Versiones que trabajan con diccionarios en lugar de listas, usando la primera fila como claves. Muy útiles cuando las columnas tienen nombres significativos.

---

## Ejemplos prácticos con archivos CSV.

•   Ejemplo 1: Calcular el promedio de edad a partir de un CSV.
    *   Asumimos un archivo personas.csv:

Nombre,Edad,Ciudad
Alice,30,Madrid
Bob,25,Barcelona
Charlie,22,Sevilla
David,40,Valencia


    *   Código Python:

import csv

edades = []
try:
    with open('personas.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

## Introducción a la Biblioteca JSON en Python

JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos que es fácil de leer y escribir para humanos, y fácil de parsear y generar para máquinas. Python incluye un módulo llamado json para trabajar con este formato.

#### Serialización (Codificación)

La serialización convierte objetos Python en una cadena JSON.

import json

#### Diccionario de ejemplo
datos_python = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["fútbol", "lectura", "viajar"],
    "casado": False
}

#### Serializar a JSON
json_string = json.dumps(datos_python, indent=4)
print(json_string)
Salida:
{
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": [
        "fútbol",
        "lectura",
        "viajar"
    ],
    "casado": false
}
#### Deserialización (Decodificación)

La deserialización convierte una cadena JSON en un objeto Python.

#### Cadena JSON de ejemplo
json_string = '{"nombre": "María", "edad": 25, "ciudad": "Barcelona"}'

#### Deserializar a Python
datos_python = json.loads(json_string)
print(datos_python)
print(type(datos_python))  # <class 'dict'>
#### Trabajar con archivos

Puedes serializar/deserializar directamente desde/hacia archivos:

#### Escribir JSON a un archivo
with open('datos.json', 'w') as archivo:
    json.dump(datos_python, archivo, indent=4)

#### Leer JSON desde un archivo
with open('datos.json', 'r') as archivo:
    datos_cargados = json.load(archivo)
#### Tipos de datos compatibles

| JSON        | Python      |
|-------------|-------------|
| object      | dict        |
| array       | list        |
| string      | str         |
| number      | int/float   |
| true/false  | True/False  |
| null        | None        |

#### Personalización de la serialización

Puedes definir cómo serializar objetos complejos:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def serializador_persona(obj):
    if isinstance(obj, Persona):
        return {'nombre': obj.nombre, 'edad': obj.edad}
    raise TypeError("Tipo no serializable")

persona = Persona("Ana", 28)
json_persona = json.dumps(persona, default=serializador_persona)
print(json_persona)  # {"nombre": "Ana", "edad": 28}
#### Consideraciones importantes

1. JSON solo soporta cadenas como claves de diccionario
2. Los objetos Python como sets, fechas o clases personalizadas no son serializables por defecto
3. Usa indent para formato legible y sort_keys para ordenar las claves
4. Para datos sensibles, considera usar ensure_ascii=False para caracteres no ASCII

El módulo JSON es ampliamente usado en APIs web, configuración de aplicaciones y almacenamiento de datos estructurados.

## Ejemplos Prácticos de Carga y Guardado de Datos en JSON

A continuación te muestro ejemplos concretos de cómo trabajar con archivos JSON en Python, incluyendo situaciones comunes.

#### 1. Guardar (serializar) datos en un archivo JSON

import json

#### Datos a guardar
usuarios = [
    {"id": 1, "nombre": "Ana", "activo": True, "puntos": 85.5},
    {"id": 2, "nombre": "Carlos", "activo": False, "puntos": 42.0},
    {"id": 3, "nombre": "María", "activo": True, "puntos": 93.2}
]

#### Guardar en archivo con formato legible
with open('usuarios.json', 'w', encoding='utf-8') as f:
    json.dump(usuarios, f, indent=2, ensure_ascii=False)
Esto creará un archivo usuarios.json con:
[
  {
    "id": 1,
    "nombre": "Ana",
    "activo": true,
    "puntos": 85.5
  },
  {
    "id": 2,
    "nombre": "Carlos",
    "activo": false,
    "puntos": 42.0
  },
  {
    "id": 3,
    "nombre": "María",
    "activo": true,
    "puntos": 93.2
  }
]
#### 2. Cargar (deserializar) datos desde un archivo JSON

import json

#### Cargar datos desde archivo
with open('usuarios.json', 'r', encoding='utf-8') as f:
    datos_cargados = json.load(f)

#### Usar los datos cargados
for usuario in datos_cargados:
    print(f"Usuario: {usuario['nombre']}, Puntos: {usuario['puntos']}")
Salida:
Usuario: Ana, Puntos: 85.5
Usuario: Carlos, Puntos: 42.0
Usuario: María, Puntos: 93.2
#### 3. Guardar configuraciones de aplicación

config = {
    "app_name": "MiApp",
    "version": "1.3.2",
    "settings": {
        "theme": "dark",
        "notifications": True,
        "max_results": 50
    },
    "last_update": "2023-11-15"
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
#### 4. Cargar configuraciones con manejo de errores

import json
import os

def cargar_configuracion():
    try:
        if not os.path.exists('config.json'):
            raise FileNotFoundError
        
        with open('config.json', 'r') as f:
            return json.load(f)
            
    except FileNotFoundError:
        print("Archivo de configuración no encontrado. Usando valores por defecto.")
        return {
            "app_name": "MiApp",
            "version": "1.0.0",
            "settings": {
                "theme": "light",
                   "notifications": False,
                "max_results": 25
            }
        }
    except json.JSONDecodeError:
        print("Error al leer el archivo de configuración. Formato inválido.")
        return None

config = cargar_configuracion()
print(config)
#### 5. Serializar objetos personalizados

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

#### Función serializadora personalizada
def serializar_producto(obj):
    if isinstance(obj, Producto):
        return {
            "id": obj.id,
            "nombre": obj.nombre,
            "precio": obj.precio,
            "_type": "Producto"
        }
    raise TypeError("Objeto no serializable")

#### Crear lista de productos
productos = [
    Producto(101, "Laptop", 999.99),
    Producto(102, "Mouse", 19.99)
]

#### Serializar y guardar
with open('productos.json', 'w') as f:
    json.dump(productos, f, default=serializar_producto, indent=2)
#### 6. Cargar y reconstruir objetos personalizados

def cargar_productos():
    def reconstruir_producto(d):
        if "_type" in d and d["_type"] == "Producto":
            return Producto(d["id"], d["nombre"], d["precio"])
        return d
    
    with open('productos.json', 'r') as f:
        return json.load(f, object_hook=reconstruir_producto)

productos_cargados = cargar_productos()
for p in productos_cargados:
    print(f"Producto: {p.nombre}, Precio: {p.precio}")
#### 7. Ejemplo con datos más complejos

`python
import json
from datetime import datetime

#### Datos complejos con fechas
ventas = {
    "fecha_actual": datetime.now(),
    "registros": [
        {
            "id_venta": "V-1001",
            "productos": [
                {"id": 101, "cantidad": 2},
                {"id": 205, "cantidad": 1}
            ],
            "total": 159.98,
            "fecha": datetime(2023, 11, 15)
        }
    ]
}

#### Serializador personalizado para fechas
def serializador_complejo(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Tipo no serializable")

#### Guardar
with open('ventas.json', 'w') as f:
    json.dump(ventas, f, default=serializador_complejo, indent=2)
`

Estos ejemplos cubren los casos más comunes de uso de JSON en Python, desde operaciones básicas hasta situaciones más avanzadas con objetos personalizados y manejo de errores.

## Cierre Automático de Archivos usando with en Python

El uso de la sentencia with es la forma recomendada de trabajar con archivos en Python, ya que garantiza el cierre automático del archivo incluso si ocurren excepciones durante las operaciones.

#### ¿Por qué usar with?

1. Cierre automático: El archivo se cierra automáticamente al salir del bloque with
2. Manejo seguro de excepciones: Si ocurre un error, el archivo se cierra correctamente
3. Código más limpio: No necesitas llamar explícitamente a close()
4. Mejor legibilidad: El contexto del manejo del archivo está claramente delimitado

#### Sintaxis básica

with open('archivo.txt', 'r') as archivo:
    # Operaciones con el archivo
    contenido = archivo.read()
    print(contenido)
    
#Aquí el archivo ya está cerrado automáticamente
#### Ejemplos con JSON

#### 1. Escritura de archivo JSON

import json

datos = {
    "nombre": "Laura",
    "edad": 28,
    "habilidades": ["Python", "SQL", "Análisis de datos"]
}

with open('datos_personales.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
#### El archivo se cierra automáticamente aquí
#### 2. Lectura de archivo JSON

import json

with open('datos_personales.json', 'r', encoding='utf-8') as archivo:
    datos_cargados = json.load(archivo)
    print(f"Nombre: {datos_cargados['nombre']}")
    print(f"Habilidades: {', '.join(datos_cargados['habilidades'])}")
    
#### El archivo se cierra automáticamente aquí
#### Múltiples archivos en un solo with

Puedes manejar varios archivos simultáneamente:

with open('origen.json', 'r') as entrada, open('copia.json', 'w') as salida:
    datos = json.load(entrada)
    json.dump(datos, salida, indent=2)
    
#### Ambos archivos se cierran automáticamente aquí
#### Beneficios frente al manejo tradicional

Comparación con el método tradicional (no recomendado):

#### Método tradicional (riesgo de olvidar cerrar el archivo)
archivo = open('datos.json', 'r')
try:
    datos = json.load(archivo)
finally:
    archivo.close()  # Fácil de olvidar
    
#### Método con with (recomendado)
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
#No necesitas recordar cerrar el archivo
#### Manejo de excepciones con with

El cierre automático funciona incluso con errores:

try:
    with open('config.json', 'r') as archivo:
        config = json.load(archivo)
        # Simular un error
        valor = 1 / 0
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error al procesar el archivo: {e}")
except ZeroDivisionError:
    print("Error matemático, pero el archivo ya está cerrado")
    
#En cualquier caso, el archivo está cerrado aquí
#### Context Manager personalizado

Puedes crear tus propios manejadores de contexto:

class ArchivoJSON:
    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        
    def __enter__(self):
        self.archivo = open(self.nombre_archivo, self.modo)
        return self.archivo
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.archivo.close()

#### Uso del manejador personalizado
with ArchivoJSON('datos.json', 'r') as archivo:
    datos = json.load(archivo)
El uso de with es una práctica esencial en Python para el manejo de recursos, no solo para archivos, sino también para conexiones de red, bases de datos y otros recursos que necesitan liberación adecuada.

## Organización y Estructura de Archivos en Proyectos Python

Una buena estructura de archivos es fundamental para mantener proyectos escalables, mantenibles y colaborativos. Aquí te presento las mejores prácticas y patrones comunes.

#### Estructura Básica Recomendada

mi_proyecto/
│
├── proyecto/                  # Paquete principal del proyecto
│   ├── __init__.py            # Hace que el directorio sea un paquete Python
│   ├── modulo_principal.py    # Módulo principal
│   ├── subpaquete/            # Subpaquetes
│   │   ├── __init__.py
│   │   └── modulo_secundario.py
│   └── utils/                 # Utilidades comunes
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                     # Tests del proyecto
│   ├── __init__.py
│   ├── test_modulo_principal.py
│   └── test_utils/
│       └── test_helpers.py
│
├── docs/                      # Documentación
│   ├── conf.py
│   └── index.rst
│
├── data/                      # Datos del proyecto
│   ├── input/                 # Datos de entrada
│   │   └── datos.json
│   └── output/                # Resultados generados
│       └── resultados.csv
│
├── config/                    # Configuraciones
│   ├── settings.json
│   └── logging.conf
│
├── .gitignore                 # Archivos a ignorar por Git
├── README.md                  # Documentación principal
├── requirements.txt           # Dependencias
├── setup.py                   # Configuración del paquete (para instalación)
└── pyproject.toml             # Configuración moderna del proyecto (opcional)
#### Estructuras para Diferentes Tipos de Proyectos

#### 1. Aplicación CLI (Command Line Interface)

cli_app/
│
├── cli_app/
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── init.py
│   │   └── process.py
│   ├── core/
│   │   └── processor.py
│   └── __main__.py           # Punto de entrada
│
├── tests/
└── setup.py
#### 2. Proyecto de Ciencia de Datos

data_science_project/
│
├── notebooks/                # Jupyter notebooks
│   ├── 01-exploracion.ipynb
│   └── 02-modelado.ipynb
│
├── src/
│   ├── data/
│   │   ├── preprocessing.py
│   │   └── cleaning.py
│   ├── features/
│   ├── models/
│   └── visualization/
│
├── data/
│   ├── raw/                  # Datos crudos (inmutables)
│   ├── processed/            # Datos transformados
│   └── external/             # Datos de terceros
│
└── reports/                  # Reportes y gráficos
#### 3. Aplicación Web (Flask/Django)

#### Estructura Flask:

flask_app/
│
├── app/
│   ├── static/               # CSS, JS, imágenes
│   ├── templates/            # Plantillas HTML
│   ├── __init__.py           # Factory de la aplicación
│   ├── auth/                 # Blueprint de autenticación
│   │   ├── routes.py
│   │   └── forms.py
│   ├── blog/                 # Blueprint de blog
│   │   ├── routes.py
│   │   └── models.py
│   └── extensions.py         # Extensiones (DB, login, etc.)
│
├── migrations/               # Migraciones de base de datos
├── instance/                 # Configuraciones por instancia
├── tests/
└── wsgi.py                   # Punto de entrada para producción
#### Estructura Django:

django_project/
│
├── project/                  # Proyecto principal
│   ├── settings/             # Configuraciones divididas
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── asgi.py/wsgi.py
│
├── apps/                     # Aplicaciones Django
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
│   └── products/
│
├── static/
├── templates/
├── manage.py
└── requirements/
    ├── base.txt
    ├── dev.txt
    └── prod.txt
#### Buenas Prácticas

1. Separación de preocupaciones: Divide el código por funcionalidad, no por tipo de archivo
2. Nombres descriptivos: Usa nombres claros para archivos y directorios
3. Jerarquía plana: Evita anidamiento excesivo de directorios
4. Documentación: Incluye READMEs en cada directorio importante
5. Configuración: Separa configuraciones por entorno (dev, test, prod)
6. Pruebas: Mantén una estructura de tests paralela a la de tu código
7. Datos: Sigue el principio de "datos crudos son sagrados" (no modificar originales)

#### Herramientas Útiles

1. Cookiecutter: Para generar estructuras de proyectos estándar ([cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage))
2. Poetry: Para gestión moderna de dependencias y empaquetado
3. Makefiles: Para automatizar tareas comunes
4. pre-commit: Para mantener estándares de código antes de cada commit

#### Ejemplo de imports organizados

En un proyecto bien estructurado, los imports se ven limpios y lógicos:

#### Import estándar
import os
import json
from datetime import datetime

#Import de terceros
import pandas as pd
from flask import Blueprint

#Import local
from proyecto.utils.helpers import validate_input
from .models import User
Una buena organización desde el principio ahorra tiempo y problemas a medida que el proyecto crece, facilita la colaboración y hace más sencillo el mantenimiento del código.
