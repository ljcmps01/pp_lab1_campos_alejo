import parcial_biblioteca as dt
import os
import platform

clean_command=str()
match platform.system():
    case 'Windows':
        clean_command='cls'
    case 'Linux':
        clean_command='clear'

lista_jugadores = dt.leer_json("dt.json","jugadores")

while True:
    lista_opciones = ["Mostrar jugadores ",
        "Mostrar estadisticas de un jugador y exportar a CSV",
        "##Guardar estadisticas en CSV",
        "",
        "",
        "",
        "",
        "",
        "",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
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
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            pass
        case 14:
            pass
        case 15:
            pass
        case 16:
            pass
        case 17:
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