#Punto 2 y 3: estan las funciones de string hechas, 
## Punto 2: (HECHO)falta hacer el submenu para elegir el jugador (listar con mostrar_jugadores, pedir al usuario elegir indice, e imprimir
# sus estadisticas)
#
## Punto 3: falta la funcion de guardado de CSV (usar guardar_archivo y generar_CSV), la funcion debe autogenerar el nombre de archivo
#
# Integrar punto 3 en punto 2? preguntar luego de imprimir en el 2, si desea guardar en CSV


import json
import re
import os

def pedir_entero(mensaje_input = "Ingrese un entero: "):
    
    entero = int()

    while True:
        str_input = input(mensaje_input)
        
        if str_input.isdecimal():
            entero = int(str_input)
            break

    return entero
    


def leer_json(nombre_archivo:str,header="")->list:
    """procesa un archivo json y guarda su informacion en una lista

    Args:
        nombre_archivo (str): ruta del archivo JSON
        header (str, optional): permite acceder directamente a un primitivo especifico . Defaults to "".

    Returns:
        list: contiene la informacion procesada en una lista
    """
    lista = list()
    with open(nombre_archivo) as archivo:
        json_archivo = json.load(archivo)

        if header != "":
            lista = json_archivo[header]
        else:
            lista = json_archivo

    return lista

def guardar_archivo(nombre_archivo:str, contenido:str())->bool:
    """Crea o sobreescribe un archivo con el contenido pasado como parametro.

    Args:
        nombre_archivo (str): nombre o ruta del archivo a generar
        contenido (str): contenido a guardar en el archivo

    Returns:
        bool: Retorna True si el archivo fue escrito correctamente, False si el archivo no pudo ser generado
    """
    success = False 
    
    with open(nombre_archivo, 'w+') as archivo:
        if archivo.write(contenido) > 0:
            success = True

    if success == True:
        print("Se creo el archivo {0}".format(nombre_archivo))
    else:
        print("ERROR al crear el archivo {0}".format(nombre_archivo))

def capitalizar(matchobj):
    """capitaliza el contenido del matchobj

    Args:
        matchobj (matchobj): matchobj de las palabras que desea capitalizards

    Returns:
        str: la palabra capitalizada
    """
    return matchobj.group(0).capitalize()

def capitalizar_palabras(contenido:str)->str:
    """Filtra la string pasada como parametro, separa las palabras, le aplica la funcion capitalizar
    y reemplaza las palabras en minusculas por capitalizadas

    Args:
        contenido (str): string a capitalizard

    Returns:
        str: copia de la string ingresada pero capitalizada
    """
    capitalizado = re.sub(r"\b[a-z]+\b", capitalizar, contenido)

    return capitalizado

def obtener_nombre_capitalizado(jugador:dict)->str:
    """Obtiene el nombre del jugador y lo capitalizada

    Args:
        jugador (dict): diccionario del jugador

    Returns:
        str: retorna una string del nombre formateado
        "Nombre: Nombre_Del_Jugador"
    """
    nombre_jugador = str()
    if "nombre" in jugador:
        nombre_jugador = "Nombre: {0}".format(capitalizar_palabras(jugador["nombre"]))
    
    return nombre_jugador

def obtener_nombre_y_dato(jugador:dict,dato:str)->str:
    """Obtiene el nombre y un dato especifico del jugador

    Args:
        jugador (dict): diccionario del jugador
        dato (str): dato que desea obtener

    Returns:
        str: string formateada con el nombre y el dato del jugador
    """
    nombre_dato_jugador = str()

    if dato in jugador:
        nombre_dato_jugador = "{0} - {1}: {2}".format(obtener_nombre_capitalizado(jugador),capitalizar_palabras(dato),jugador[dato])
    
    return nombre_dato_jugador

def mostrar_todos_nombre_dato(lista_jugadores:list,dato:str, enumerar = False)->int:
    """itera sobre todos los jugadores en una lista y extrae el nombre y un dato

    Args:
        lista_jugadores (list): lista de jugadores a mostrar
        dato (str): dato a obtener
        enumerar (bool): si es True, mostrara un prefijo previo al jugador

    Returns:
        int: retorna True si se pudo mostrar al menos un jugador, False en caso de que la lista este vacia
    """
    
    contador = 0

    if lista_jugadores != list():
        if enumerar:
            for jugador in lista_jugadores:
                
                print("{0} - {1}".format(contador+1,obtener_nombre_y_dato(jugador, dato)))
                contador+=1

        else:
            for jugador in lista_jugadores:
                print(obtener_nombre_y_dato(jugador, dato))
                contador+=1
    
    return contador

def obtener_nombre_estadisticas_jugador(jugador:dict):
    lista_estadisticas = ["{0}: {1}".format(capitalizar_palabras(estadistica),jugador["estadisticas"][estadistica]) for estadistica in jugador["estadisticas"]]
    str_jugador = "{0}\n{1}".format(obtener_nombre_capitalizado(jugador),"\n".join(lista_estadisticas))

    return str_jugador
        
def guardar_CSV_estadistica(jugador:dict)->bool:
    
    nombre_archivo = "estadisticas_{0}.csv".format(jugador["nombre"])
    str_estadisticas = generar_CSV_estadisticas(jugador)

    return guardar_archivo(nombre_archivo, str_estadisticas)


def generar_CSV_estadisticas(jugador:dict)->str:
    """genera un string con las estadisticas del jugador

    Args:
        jugador (dict): jugador a generar

    Returns:
        str: string con el contenido del diccionario con formato CSV
    """
    lista_keys = list(jugador.keys())
    lista_keys.remove("estadisticas")
    lista_keys.remove("logros")

    lista_values = [valor for valor in jugador.values() if type(valor) is str ]


    lista_keys.extend(list(jugador["estadisticas"].keys()))
    lista_values.extend([str(estadistica) for estadistica in jugador["estadisticas"].values()])

    str_keys = ",".join(lista_keys)
    str_values = ",".join(lista_values)

    string_CSV = "{0}\n{1}".format(str_keys,str_values)

    return string_CSV

def seleccionar_mostrar_estadisticas_jugador(lista_jugadores:list)->str:
    size = mostrar_todos_nombre_dato(lista_jugadores, "posicion",True)
    str_input = input("ingrese el indice del jugador ")
    
    str_estadistica_jugador = str()
    
    indice_input = -1

    if str_input.isdecimal() and int(str_input) in range(1,size):
        indice_input = int(str_input)-1
        str_estadistica_jugador = obtener_nombre_estadisticas_jugador(lista_jugadores[indice_input])
    else:
        str_estadistica_jugador = "Opcion no valida"
        
    print(str_estadistica_jugador)

    return indice_input

def seleccionar_guardar_y_mostrar_estadisticas_jugador(lista_jugadores):
    indice_jugador = seleccionar_mostrar_estadisticas_jugador(lista_jugadores)

    if indice_jugador != -1:
        guardar = input("Desea guardar la información del jugador? (y/n)").lower()

        if guardar == "y" or guardar == "s":
            guardar_CSV_estadistica(lista_jugadores[indice_jugador])

lista_jugadores = leer_json("dt.json","jugadores")

# print(mostrar_todos_nombre_dato(lista_jugadores, "posicion",True))

#seleccionar_guardar_y_mostrar_estadisticas_jugador(lista_jugadores)

# print(generar_CSV_jugador(lista_jugadores[2]))

