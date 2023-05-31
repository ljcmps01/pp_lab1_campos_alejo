"""
#Agregar funcion de menu principal

#Documentar

#Hacer bonus

#Revisar funcion generar y guardar CSV (hacer mas generica y determinar una estructura sobre la que trabajar(lista de dict?))
"""
import json
import re
import os
from typing import Callable

#-----------------------------Archivos-----------------------------------
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
        
    return success

def generar_CSV_estadisticas(jugador:dict)->str:
    """genera un string con las estadisticas del jugador

    Args:
        jugador (dict): jugador a generar

    Returns:
        str: string con el contenido del diccionario con formato CSV
    """
    lista_keys = list()
    lista_values = list()
    
    for key,value in jugador.items() :
        if type(value) is not list:
            lista_keys.append(key)
            lista_values.append(str(value))

    str_keys = ",".join(lista_keys)
    str_values = ",".join(lista_values)

    string_CSV = "{0}\n{1}".format(str_keys,str_values)

    return string_CSV
        
def guardar_CSV_estadistica(jugador:dict)->bool:
    """Genera un CSV con las estadisticas del jugador pasado como parametro

    Args:
        jugador (dict): diccionario del jugador a guardar

    Returns:
        bool: Retorna True si el archivo fue generado exitosamente, caso contrario retorna False
    """
    
    nombre_archivo = "estadisticas_{0}.csv".format(jugador["nombre"]).replace(" ","_")
    str_estadisticas = generar_CSV_estadisticas(jugador)

    return guardar_archivo(nombre_archivo, str_estadisticas)
    #--------------------------------------------

#--------------------Validaciones-------------
def pedir_entero(mensaje_input = "Ingrese un entero: "):
    """Pide al usuario un input hasta que ingrese un entero para

    Args:
        mensaje_input (str, optional): Mensaje a mostrar al usuario al pedir el input. Defaults to "Ingrese un entero: ".

    Returns:
        int: retorna el entero ingresado
    """
    
    entero = int()

    while True:
        str_input = input(mensaje_input)
        
        if str_input.isdecimal():
            entero = int(str_input)
            break

    return entero
    
def ingresar_float(mensaje_input:str):
    """Pide al usuario un input hasta que ingrese un numero, acepta decimales separados por . o ,

    Args:
        mensaje_input (str): _description_

    Returns:
        float: retorna el numero ingresado y convertido a float
    """
    while True:
        numero = input(mensaje_input)
        if buscar_patron('^([0-9]*)(\.|,*)([0-9]+)$', numero):
            return float(numero.replace(",","."))
        else:
            print("Ingreso invalido.")
    #--------


#----------------------------manipulacion strings------------------------------------
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

def obtener_nombre_y_dato(jugador:dict,dato:str,sufijo="")->str:
    """Obtiene el nombre y un dato especifico del jugador

    Args:
        jugador (dict): diccionario del jugador
        dato (str): dato que desea obtener
        
    Returns:
        str: string formateada con el nombre y el dato del jugador
    """
    nombre_jugador = obtener_nombre_capitalizado(jugador)
    dato_jugador = str()
    nombre_dato_jugador = str()

    if dato in jugador:
        dato_jugador = "{0}: {1}{2}".format(capitalizar_palabras(dato.replace("_", " ")),jugador[dato],sufijo)
    
    if dato_jugador == str():
        dato_jugador = "dato({0}) no encontrado".format(dato)

    nombre_dato_jugador = "{0} - {1}".format(nombre_jugador,dato_jugador)

    return nombre_dato_jugador

def mostrar_todos_nombre_dato(lista_jugadores:list,dato:str, enumerar = False, sufijo="")->int:
    """itera sobre todos los jugadores en una lista y extrae el nombre y un dato

    Args:
        lista_jugadores (list): lista de jugadores a mostrar
        dato (str): dato a obtener
        para acceder al dato deseado
        enumerar (bool): si es True, mostrara un prefijo previo al jugador

    Returns:
        int: retorna True si se pudo mostrar al menos un jugador, False en caso de que la lista este vacia
    """
    
    contador = 0

    if lista_jugadores != list():
        if enumerar:
            for jugador in lista_jugadores:
                
                print("{0} - {1}{2}".format(contador+1,obtener_nombre_y_dato(jugador, dato)))
                contador+=1

        else:
            for jugador in lista_jugadores:
                print(obtener_nombre_y_dato(jugador, dato,sufijo = sufijo))
                contador+=1
    
    return contador
    #----------------------------------------------------------------

#--------------------------Funciones maximos (Punto 7:9,13,14)--------------------------------------
def calcular_max(lista_jugadores:list, estadistica: str, ascendiente = True)->dict:
    """Obtiene el jugador que contiene la campo pasado como parametro con mayor valor

    Args:
        lista_jugadores (list): lista de jugadores a analizar
        estadistica (str): campo sobre el que buscar maximo
        ascendiente (bool, optional): Indica si es ascendiente(true) o descendiente(false). Defaults to True.

    Returns:
        dict: retorna el jugador maximo
    """
    extremo_jugador = dict()
    extremo_value = None

    for jugador in lista_jugadores:
        if estadistica in jugador and (extremo_value is None or ((jugador[estadistica] > extremo_value) is ascendiente)):
            extremo_jugador = jugador
            extremo_value = jugador[estadistica]
    
    return extremo_jugador

def obtener_mostrar_jugador_maximo(lista_jugadores:list, estadistica:str)->str:
    """busca el maximo de cierta estadistica e imprime el nombre de dicho jugador junto con el valor

    Args:
        lista_jugadores (list): lista de jugadores a analizar
        estadistica (str): campo sobre el que buscar el maximo

    Returns:
        str: retorna una string formateada con nombre y estadistica
    """
    jugador_maximo = calcular_max(lista_jugadores, estadistica) 
    
    return obtener_nombre_y_dato(jugador_maximo, estadistica)
    #--------------------------Fin (puntos 7:9,13,14)--------------------------------------




#--------------------------ordenamiento--------------------------------------

def merge_estadisticas(jugador:dict)->dict:
    """Sube un nivel los campos encontrados dentro del diccionario estadistica y elimina el diccionario estadistica

    Args:
        jugador (dict): jugador sobre el cual se desea extraer las estadisticas

    Returns:
        dict: retorna el jugador generado
    """
    aux_jugador = dict(jugador)

    if "estadisticas" in jugador:
        for estadistica,valor in aux_jugador["estadisticas"].items():
            aux_jugador.update({estadistica:valor})
        del aux_jugador["estadisticas"]

    else:
        print("no se encontró el campo 'estadisticas'")

    return aux_jugador

def merge_all_estadisticas (lista_jugadores:list)->list:
    """Extra el campo estadistica de todos los jugadores dentro de la lista pasada como parametro

    Args:
        lista_jugadores (list): lista de jugadores a extraer

    Returns:
        list: retorna la lista con las estadisticas extraidas
    """
    aux_jugadores = list()

    for jugador in lista_jugadores:
        aux_jugadores.append(merge_estadisticas(jugador))
    
    return aux_jugadores
        

def comparar_strings(primer_str:str,segunda_str:str)->bool:
    """Recibe dos strings y compara si la primera es mayor que la segunda

    Args:
        primer_str (str): 
        segunda_str (str): 

    Returns:
        bool: True si la primera es mayor que la segunda, False caso contrario
    """

    primer_str_minuscula = primer_str.lower()
    segunda_str_minuscula = segunda_str.lower()

    return primer_str_minuscula > segunda_str_minuscula

def comparar_numero(primer_numero, segundo_numero):
    return primer_numero > segundo_numero

def burbujeo_jugadores(lista_jugadores:list,dato:str,orden_criterio:Callable,ascendiente = True)->list:    
    """Realiza un ordenamiento tipo burbujeo sobre la lista de jugadores

    Args:
        lista_jugadores (list): lista de jugadores a ordenar
        dato (str): campo sobre el cual comparar
        orden_criterio (Callable): criterio a aplicar (comparar strings o numeros)
        ascendiente (bool, optional): True si es orden ascendiente, False si es orden descendiente. Defaults to True.

    Returns:
        list: lista ordenada segun los parametros dados
    """
    lista_ordenada = list(lista_jugadores)
    n = len(lista_ordenada)

    for i in range(n):
        # Flag para chequear si hubo un swappeo
        swap = False
        
        # Itero sobre los elementos
        for j in range(0, n-i-1):
            jugador_a = lista_ordenada[j]
            jugador_b = lista_ordenada[j+1]
             
            if ascendiente is orden_criterio(jugador_a[dato], jugador_b[dato]):
                # Swap elementos
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
                swap = True

                
        #Si no se swappeo en la iteracion, la lista ya está ordenada 
        if not swap:
            break
    return lista_ordenada

#----------------------------Fin ordenamiento------------------------------------

#----------------------------Funciones umbral------------------------------------

def comprobar_umbral(jugador:dict, dato:str, umbral)->bool:
    """Comprueba si el jugador supera el umbral en el dato dado

    Args:
        jugador (dict): 
        dato (str): 
        umbral (_type_): 

    Returns:
        bool: True si lo supera, False si es menor o igual
    """
    return (dato in jugador) and (type(jugador[dato]) in [float,int]) and (jugador[dato] > umbral)

def obtener_superadores_umbral(lista_jugadores:dict, dato:str, umbral)->list:
    """Obtiene una lista con los jugadores que superan el umbral dado en el campo pasado como parametro

    Args:
        lista_jugadores (dict): lista de jugadores a analizar
        dato (str): campo a analizar
        umbral (float,int): umbral a comparar

    Returns:
        list: lista con los jugadores que superan el umbral
    """
    lista_superadores = list()
    for jugador in lista_jugadores:
        if dato in jugador and comprobar_umbral(jugador, dato, umbral):
            lista_superadores.append(jugador)
    return lista_superadores

def pedir_umbral_y_obtener_superadores(lista_jugadores:list, dato:str)->list:
    """Pide al usuario que ingrese un umbral y obtiene los jugadores que lo superan

    Args:
        lista_jugadores (list): lista de jugadores a analizar
        dato (str): campo a analizar

    Returns:
        list: lista de jugadores que superan el umbral
    """
    umbral = ingresar_float("Ingrese umbral de {0}: ".format(dato.replace("_"," ")))
    
    lista_superadores = obtener_superadores_umbral(lista_jugadores, dato, umbral)

    if lista_superadores == list():
        print("No se encontraron jugadores que superen {0} {1} ".format(umbral, dato.replace("_", " ")).replace(" porcentaje","%"))
    
    return lista_superadores
    #--------------------------------Fin umbral--------------------------------------

#--------------------------------Calcular promedio-----------------------------------

def calcular_promedio_dato(lista_jugadores:list, dato:str)->float:
    """Calcula el promedio con los jugadores dados y con el campo elegido

    Args:
        lista_jugadores (list): lista de jugadores a analizar
        dato (str): campo a analizar

    Returns:
        float: valor promedio, retorna 0 si se pasa una lista vacia
    """
    promedio = 0
    size = len(lista_jugadores)
    acumulador=0


    if size > 0:
        for jugador in lista_jugadores:
            if dato in jugador:
                acumulador += jugador[dato]
        promedio = acumulador / size

    return promedio

    #--------------------------------Fin calculo promedio--------------------------------

#--------------------------------Re-Gex/Busqueda--------------------------------

def buscar_patron(patron:str, entrada:str)->bool:
    """Comprueba si la string dada como parametro cumple con el patron

    Args:
        patron (str): patron a buscar
        entrada (str): string a analizar

    Returns:
        bool: True si hubo match, False caso contrario
    """
    if re.findall(patron, entrada) != list():
        return True
    else:
        return False
    
def buscar_jugador(lista_jugadores:list):
    """Pide al usuario que ingrese un nombre a buscar, obtiene las coincidencias mas cercanas(minimo 3 caracteres)
    Tambien permite buscar jugadores que comiencen con un caracter o un par, si y solo si el input es de ese largo

    Args:
        lista_jugadores (list): lista de jugadores a analizar

    Returns:
        list: lista de jugadores que matchearon con el input del usuario
    """
    nombre_ingresado = input("Ingrese el nombre del jugador: ").lower()
    len_input = len(nombre_ingresado)
    lista_matches= []
    while len(nombre_ingresado) > 2 or (len_input < 3 and len(nombre_ingresado)>0):
        for jugador in lista_jugadores:
            if buscar_patron("^{0}.| {0}.".format(nombre_ingresado), jugador["nombre"].lower()):
                lista_matches.append(jugador)

        if len(lista_matches) > 0:
            break
        nombre_ingresado = nombre_ingresado[:-1]

    return lista_matches

    #----------------------------------------------------------------

#------------------------------Punto 2 y 3----------------------------------
def obtener_nombre_estadisticas_jugador(jugador:dict)->str:
    """Obtiene todas las estadisticas de un jugador y las guarda en un string

    Args:
        jugador (dict): jugador a analizar

    Returns:
        str: string formateada con el nombre y sus estadisticas
    """
    lista_estadisticas = ["{0}: {1}".format(capitalizar_palabras(dato.replace("_"," ")),\
        jugador[dato]) for dato in jugador if type(jugador[dato]) in [int,float]]

    str_jugador = "{0}\n{1}".format(obtener_nombre_capitalizado(jugador),"\n".join(lista_estadisticas))

    return str_jugador


def seleccionar_mostrar_estadisticas_jugador(lista_jugadores:list)->int:
    """Muestra una lista enumerada de jugadores y pide al usuario seleccionar el indice
    de uno e imprime las estadisticas del mismo

    Args:
        lista_jugadores (list): lista que contiene los diccionarios de jugadores

    Returns:
        int: retorna el indice del jugador seleccionado
    """
    size = mostrar_todos_nombre_dato(lista_jugadores, "posicion", enumerar=True)
    indice_jugador = pedir_entero(mensaje_input="ingrese el indice del jugador ")
    
    str_estadistica_jugador = str()
    
    if indice_jugador in range(1,size+1):
        indice_jugador -= 1
        str_estadistica_jugador = obtener_nombre_estadisticas_jugador(lista_jugadores[indice_jugador])
    else:
        str_estadistica_jugador = "Opcion no valida"
        indice_jugador = -1
        
    print(str_estadistica_jugador)

    return indice_jugador

def seleccionar_guardar_y_mostrar_estadisticas_jugador(lista_jugadores:list):
    """Muestra la lista de nombres de  jugadores y pide al usuario seleccionar uno,
    imprime sus estadisticas y luego consulta si desea guardar la informacion en un archivo
    CSV

    Args:
        lista_jugadores (list): lista de jugadores a analizar
    """
    indice_jugador = seleccionar_mostrar_estadisticas_jugador(lista_jugadores)

    if indice_jugador != -1:
        guardar = input("Desea guardar la información del jugador? (y/n)").lower()

        if guardar == "y" or guardar == "s":
            guardar_CSV_estadistica(lista_jugadores[indice_jugador])

#--------------------------Punto 2 y 3--------------------------------------


#-------------------------------Punto 6------------------------------
def pertenece_hof(jugador:dict):
    return "logros" in jugador and "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]

def pedir_nombre_y_comprobar_hof(lista_jugadores):
    lista_resultado_busqueda = buscar_jugador(lista_jugadores)

    for jugador in lista_resultado_busqueda:
        if pertenece_hof(jugador):
            print("{0} pertenece al salon de la fama".format(jugador["nombre"]))
        else:
            print("{0} NO pertenece al salon de la fama".format(jugador["nombre"]))

    #--------------------------------Punto 6--------------------------------


#--------------------------Punto 17--------------------------------------



def contar_logros_jugador(jugador:dict)->dict:
    """obtiene la cantidad de logros del jugador

    Args:
        jugador (dict): jugador a analizar

    Returns:
        dict: diccionario con el nombre y cantidad de logos
    """
    jugador_logros = {"nombre": str(),"cantidad_logros":int()}
    nombre_jugador = obtener_nombre_capitalizado(jugador)
    acumulador_logros = 0
    for logro in jugador["logros"]:
        if buscar_patron("^[0-9]+ veces", logro):
            numero = int(re.sub(" veces.*","",logro))
            acumulador_logros += numero
        else:
            acumulador_logros += 1
    
    return {"nombre": jugador["nombre"],"cantidad_logros": acumulador_logros}

def obtener_todos_cantidad_logros(lista_jugadores:list)->list:
    """Analiza toda la lista de jugadores y obtiene la cantidad de logros de todos los jugadores

    Args:
        lista_jugadores (list): lista de jugadores a analizar

    Returns:
        list: lista con los nombres y cantidad de logros de cada jugador
    """
    lista_logros = list()

    for jugador in lista_jugadores:
        lista_logros.append(contar_logros_jugador(jugador))

    return lista_logros

def obtener_logros_maximo(lista_jugadores):
    jugador_maximo = calcular_max(obtener_todos_cantidad_logros(lista_jugadores), "cantidad_logros")

    return obtener_nombre_y_dato(jugador_maximo, "cantidad_logros")

#--------------------------FIN punto 17--------------------------------------

#--------------------------------Punto 20--------------------------------
def separar_por_posicion(lista_jugadores:list)->dict:
    """Divide la lista de jugadores en distintos diccionarios segun su posicion

    Args:
        lista_jugadores (list): lista de jugadores a analizar

    Returns:
        dict: diccionario de listas con la posicion como llave y lista de los jugadores que poseen esa posicion  
    """
    lista_ordenada = burbujeo_jugadores(lista_jugadores, "posicion", comparar_strings)
    posicion_actual = str()
    diccionario_posicion = dict()
    for jugador in lista_ordenada:
        if jugador["posicion"] == posicion_actual:
            diccionario_posicion[posicion_actual].append(jugador)
        else:
            posicion_actual = jugador["posicion"]
            diccionario_posicion.update({posicion_actual:[jugador]})
        
    return diccionario_posicion
    #---------------------------------Fin punto 20-------------------------------

#---------------------------------PUNTO EXTRA 23-------------------------------
def obtener_lista_ranking_dato(lista_jugadores:list,dato:str)->int:
    lista_ordenada = burbujeo_jugadores(lista_jugadores, dato, comparar_numero, ascendiente = False)
    lista_ranking = list()
    contador = 1
    for jugador in lista_ordenada:
        lista_ranking.append({"nombre": jugador["nombre"], 
        dato.split("_")[0]:contador})
        contador+=1
    return lista_ranking

def merge_diccionarios(jugador_a,jugador_b):
    diccionario_fusionado = dict()

    for campo_a,valor_a in jugador_a.items():
        if not (campo_a in diccionario_fusionado.keys()):
            diccionario_fusionado.update({campo_a: valor_a})
    for campo_b,valor_b in jugador_b.items():
        if not (campo_b in diccionario_fusionado.keys()):
            diccionario_fusionado.update({campo_b: valor_b})
    
    return diccionario_fusionado

def merge_lista_diccionarios(lista_a,lista_b,dato):
    lista_fusionada = list()

    for jugador_a in lista_a:
        for jugador_b in lista_b:
            if jugador_a[dato] == jugador_b[dato]:
                lista_fusionada.append(merge_diccionarios(jugador_a, jugador_b))
    
    return lista_fusionada


def lista_dict_a_csv(lista_jugadores):
    str_csv = str() 
    if len(lista_jugadores) > 0:
        lista_header = list(lista_jugadores[0].keys())
        str_csv += ",".join(lista_header)+"\n"

        for jugador in lista_jugadores:
            str_csv += ",".join([str(valor) for valor in jugador.values()])+"\n"

    return str_csv

def generar_lista_ranking(lista_jugadores,lista_campos):
    lista_rankings = list()

    for campo in lista_campos:
        if lista_rankings == list():
            lista_rankings=obtener_lista_ranking_dato(lista_jugadores, campo)
        else:
            lista_aux = obtener_lista_ranking_dato(lista_jugadores, campo)
            lista_rankings = merge_lista_diccionarios(lista_rankings, lista_aux, "nombre")
    
    return lista_rankings 

def guardar_csv_ranking(lista_jugadores, lista_campos, nombre_archivo = "lista_rankings"):
    lista_rankings = generar_lista_ranking(lista_jugadores, lista_campos)
    str_rankings = lista_dict_a_csv(lista_rankings)

    if not (nombre_archivo.endswith(".csv")):
        nombre_archivo+=".csv"

    return guardar_archivo(nombre_archivo, str_rankings)

    #---------------------------------FIN EXTRA 23-------------------------------


#punto 4 extra

def obtener_promedio_ranking(lista_jugadores,lista_campos):
    lista_ranking=generar_lista_ranking(lista_jugadores, lista_campos)
    lista_promedio_ranking = list()

    for jugador in lista_ranking:
        acum_ranking = 0
        ranking_jugador=dict()
        n_campos = 0

        for campo,valor in jugador.items():
            if type(valor) == str:
                ranking_jugador.update({"nombre":valor})
            else:
                acum_ranking+=valor
                n_campos+=1

            if n_campos!=0:
                ranking_jugador.update({"ranking_promedio":acum_ranking/n_campos})
            else:
                ranking_jugador.update({"ranking_promedio":0})
        lista_promedio_ranking.append(ranking_jugador)

    return lista_promedio_ranking
    #punto 4 extra
        

#punto 2 extra

def check_AS(jugador):
    flag_AS = False
    string_AS = str()
    n_AS = 0
    if "logros" in jugador:
        for logro in jugador["logros"]:
            if buscar_patron(".*All Star$", logro.replace("-", " ")):
                flag_AS = True
                string_AS = logro
                break
        if flag_AS:
            n_AS = int(re.findall("^[0-9]+", string_AS)[0])
    
    return n_AS

def obtener_AS_jugadores(lista_jugadores):
    lista_cantidad_as = list()
    for jugador in lista_jugadores:
        lista_cantidad_as.append({"nombre": jugador["nombre"], "veces_all_star": check_AS(jugador)})
    
    return lista_cantidad_as

def mostrar_cantidad_as_por_jugador(lista_jugadores):
    lista_ordenada = burbujeo_jugadores(obtener_AS_jugadores(lista_jugadores), "veces_all_star", comparar_numero, ascendiente=False)

    for jugador in lista_ordenada:
        print("{0} ({1} veces All Star)".format(jugador["nombre"],jugador["veces_all_star"]))


    #punto 2 extra


def menu_dt():
    print(
        "1 - Mostrar jugadores \
        \n2 - Mostrar estadisticas de un jugador y exportar a CSV\
        \n3 - Guardar estadisticas en CSV\
        \n4 - buscar un jugador por su nombre y mostrar sus logros como campeonatos de la NBAparticipaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto\
        \n5 - Mostrar el promedio de puntos por partido del equipo y mostrar el individual de cada jugador\
        \n6 - Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto\
        \n7 - Mostrar jugador con la mayor cantidad de rebotes totales\
        \n8 - Mostrar el jugador con el mayor porcentaje de tiros de campo\
        \n9 - Mostrar el jugador con la mayor cantidad de asistencias totales\
        \n10 - Ingresar umbral y mostrar superadores de promedio de puntos por partido \
        \n11 - Ingresar umbral y mostrar superadores de promedio de rebotes \
        \n12 - Ingresar umbral y mostrar superadores de promedio de asistencias \
        \n13 - Mostrar el jugador con la mayor cantidad de robos totales\
        \n14 - mostrar el jugador con la mayor cantidad de bloqueos totales\
        \n15 - Ingresar umbral y mostrar superadores de porcentaje de tiros libres\
        \n16 - Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\
        \n17 - Mostrar el jugador con la mayor cantidad de logros obtenidos\
        \n18 - Ingresar umbral y mostrar superadores de porcentaje de tiros triples \
        \n19 - Mostrar el jugador con la mayor cantidad temporadas jugadas\
        \n20 - Ingresar umbral y mostrar superadores de porcentaje de tiros de campo por posicion\
        \n23 - Crear csv con los rankings de puntos, rebotes, asistencias y robos de cada jugador \
        \n24 - Cantidad de jugadores por posicion\
        \n26: #extra 3 - mostrar maximos de estadisticas formateados\
        \n27: #extra 4 - mostrar jugador con mejores estadisticas promedio\
        \n21 - salir\n\n")


    opcion = pedir_entero(mensaje_input = "Ingrese una opcion: ")
    
    return opcion

lista_jugadores = leer_json("dt.json","jugadores")
lista_jugadores = merge_all_estadisticas(lista_jugadores)

print(check_AS(lista_jugadores[-1]))

# mostrar_todos_nombre_dato(buscar_jugador(lista_jugadores), "posicion")