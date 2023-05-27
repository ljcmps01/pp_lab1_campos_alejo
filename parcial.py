import parcial_biblioteca as dt
from parcial_biblioteca import lista_jugadores
import os
import platform

clean_command=str()
match platform.system():
    case 'Windows':
        clean_command='cls'
    case 'Linux':
        clean_command='clear'

#lista_jugadores = dt.leer_json("dt.json","jugadores")

while True:
    lista_opciones = ["Mostrar jugadores ",
        "Mostrar estadisticas de un jugador y exportar a CSV",
        "##Guardar estadisticas en CSV",
        "",
        "",
        "",
        "Mostrar jugador con la mayor cantidad de rebotes totales",
        "Mostrar el jugador con el mayor porcentaje de tiros de campo",
        "Mostrar el jugador con la mayor cantidad de asistencias totales",
        " ",
        " ",
        " ",
        "Mostrar el jugador con la mayor cantidad de robos totales",
        "mostrar el jugador con la mayor cantidad de bloqueos totales",
        " ",
        " ",
        "Mostrar el jugador con la mayor cantidad de logros obtenidos",
        " ",
        " ",
        " ",
        "salir"]

    for i in range(len(lista_opciones)) :
        print("{0} - {1}".format(i+1, lista_opciones[i]))

    opcion = dt.pedir_entero(mensaje_input = "Ingrese una opcion: ")

    match opcion:
        case 1:     #"Mostrar jugadores ",
            dt.mostrar_todos_nombre_dato(lista_jugadores, "posicion")
            pass
        case 2:     #"Mostrar estadisticas de un jugador y exportar a CSV",
            dt.seleccionar_guardar_y_mostrar_estadisticas_jugador(lista_jugadores)
            pass
        case 3:     ##Guardar estadisticas en CSV",
            dt.seleccionar_guardar_y_mostrar_estadisticas_jugador(lista_jugadores)
            pass
        case 4:

            pass
        case 5:

            pass
        case 6:

            pass
        case 7:     #Mostrar jugador con la mayor cantidad de rebotes totales
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "rebotes_totales"))
            pass

        case 8:     #"Mostrar el jugador con el mayor porcentaje de tiros de campo"
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "porcentaje_tiros_de_campo"))
            pass

        case 9:     #Mostrar el jugador con la mayor cantidad de asistencias totales",
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "asistencias_totales"))
            pass

        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:    #Mostrar el jugador con la mayor cantidad de robos totales",
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "robos_totales"))
            pass
        case 14:    #Mostrar el jugador con la mayor cantidad de bloqueos totales",
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "bloqueos_totales"))
        
            pass
        case 15:
            pass
        case 16:
            pass
        case 17:    #mostrar el jugador con la mayor cantidad de logros obtenidos
            print(dt.obtener_logros_maximo(lista_jugadores))
            pass
        case 18:
            pass
        case 19:
            pass
        case 20:
            pass
        case 21:
            break
        case 23:
            pass
        case _:
            print("Ingrese una opcion valida")
            pass

    input("Presione enter para continuar")
    os.system(clean_command)