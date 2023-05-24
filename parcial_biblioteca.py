#Punto 2 y 3: estan las funciones de string hechas, 
## Punto 2: falta hacer el submenu para elegir el jugador (listar con mostrar_jugadores, pedir al usuario elegir indice, e imprimir
# sus estadisticas)
#
## Punto 3: falta la funcion de guardado de CSV (usar guardar_archivo y generar_CSV), la funcion debe autogenerar el nombre de archivo


import json
import re
import os

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

def mostrar_todos_nombre_dato(lista_jugadores:list,dato:str, enumerar = False)->bool:
    """itera sobre todos los jugadores en una lista y extrae el nombre y un dato

    Args:
        lista_jugadores (list): lista de jugadores a mostrar
        dato (str): dato a obtener
        enumerar (bool): si es True, mostrara un prefijo previo al jugador

    Returns:
        bool: retorna True si se pudo mostrar al menos un jugador, False en caso de que la lista este vacia
    """
    success = False

    contador = 1

    if lista_jugadores != list():
        if enumerar:
            for jugador in lista_jugadores:
                
                print("{0} - {1}".format(contador,obtener_nombre_y_dato(jugador, dato)))
                contador+=1

        else:
            for jugador in lista_jugadores:
                print(obtener_nombre_y_dato(jugador, dato))

        success = True
    
    return success

def obtener_nombre_estadisticas_jugador(jugador:dict):
    lista_estadisticas = ["{0}: {1}".format(capitalizar_palabras(estadistica),jugador["estadisticas"][estadistica]) for estadistica in jugador["estadisticas"]]
    str_jugador = "{0}\n{1}".format(obtener_nombre_capitalizado(jugador),"\n".join(lista_estadisticas))

    return str_jugador
        

def generar_CSV_jugador(jugador:dict)->str:
    """genera un string con las estadisticas del jugador

    Args:
        jugador (dict): jugador a generar

    Returns:
        str: string con el contenido del diccionario con formato CSV
    """
    lista_keys = list(jugador.keys())
    lista_keys.remove("estadisticas")
    lista_keys.remove("logros")

    lista_values = [valores for valores in lista_keys]

    lista_keys.extend(list(jugador["estadisticas"].keys()))
    lista_values.extend([str(estadistica) for estadistica in jugador["estadisticas"].values()])

    str_keys = ",".join(lista_keys)
    str_values = ",".join(lista_values)

    string_CSV = "{0}\n{1}".format(str_keys,str_values)

    return string_CSV

lista_jugadores = leer_json("dt.json","jugadores")

# print(mostrar_todos_nombre_dato(lista_jugadores, "posicion",True))

print(obtener_nombre_estadisticas_jugador(lista_jugadores[2]))

# print(generar_CSV_jugador(lista_jugadores[2]))

