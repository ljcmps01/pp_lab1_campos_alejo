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

    match dt.menu_dt():
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
            lista_matches = dt.buscar_jugador(lista_jugadores)
            for jugador in lista_matches:
                print("{0}\n{1}\n\n".format(dt.obtener_nombre_capitalizado(jugador), "\n".join(jugador["logros"])))
            
                
        case 5:     #Mostrar el promedio de puntos por partido del equipo y mostrar el individual de cada jugador
            lista_ordenada = dt.burbujeo_jugadores(lista_jugadores, "nombre", dt.comparar_strings)
            
            print("El promedio de puntos por partido es de {0} puntos".format(
                dt.calcular_promedio_dato(lista_ordenada, "promedio_puntos_por_partido")))

            pass
        case 6:     #Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto
            dt.pedir_nombre_y_comprobar_hof(lista_jugadores)
            pass
        case 7:     #Mostrar jugador con la mayor cantidad de rebotes totales
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "rebotes_totales"))
            pass

        case 8:     #"Mostrar el jugador con el mayor porcentaje de tiros de campo"
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "porcentaje_tiros_de_campo",sufijo='%'))
            pass

        case 9:     #Mostrar el jugador con la mayor cantidad de asistencias totales",
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "asistencias_totales"))
            pass

        case 10:    #Ingresar umbral y mostrar superadores de promedio de puntos por partido ",
            lista_superadores = dt.pedir_umbral_y_obtener_superadores(lista_jugadores, "promedio_puntos_por_partido")
            dt.mostrar_todos_nombre_dato(lista_superadores, "promedio_puntos_por_partido")
            

        case 11:    # "Ingresar umbral y mostrar superadores de promedio de rebotes ",
            lista_superadores = dt.pedir_umbral_y_obtener_superadores(lista_jugadores, "promedio_rebotes_por_partido")
            dt.mostrar_todos_nombre_dato(lista_superadores, "promedio_rebotes_por_partido")

        case 12:    # "Ingresar umbral y mostrar superadores de promedio de asistencias ",
            lista_superadores = dt.pedir_umbral_y_obtener_superadores(lista_jugadores, "promedio_asistencias_por_partido")
            dt.mostrar_todos_nombre_dato(lista_superadores, "promedio_asistencias_por_partido")

        case 13:    #Mostrar el jugador con la mayor cantidad de robos totales",
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "robos_totales"))

        case 14:    #Mostrar el jugador con la mayor cantidad de bloqueos totales",
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "bloqueos_totales"))
        
            pass
        case 15:    #Ingresar umbral y mostrar superadores de porcentaje de tiros libres
            lista_superadores = dt.pedir_umbral_y_obtener_superadores(lista_jugadores, "porcentaje_tiros_libres")
            dt.mostrar_todos_nombre_dato(lista_superadores, "porcentaje_tiros_libres",sufijo='%')

        case 16:    #Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido
            lista_ordenada = dt.burbujeo_jugadores(lista_jugadores, "promedio_puntos_por_partido", dt.comparar_numero, ascendiente=False)
            lista_ordenada.pop()

            print("Quitando el jugador con menor promedio, el promedio de puntos por partido es de {0} puntos".format(dt.calcular_promedio_dato(
                lista_ordenada, "promedio_puntos_por_partido")))
            pass
        case 17:    #mostrar el jugador con la mayor cantidad de logros obtenidos
            print(dt.obtener_logros_maximo(lista_jugadores))
            pass
        case 18:    #Ingresar umbral y mostrar superadores de porcentaje de tiros triples
            lista_superadores = dt.pedir_umbral_y_obtener_superadores(lista_jugadores, "porcentaje_tiros_triples")
            dt.mostrar_todos_nombre_dato(lista_superadores,  "porcentaje_tiros_triples",sufijo='%')

        case 19:    #Mostrar el jugador con la mayor cantidad temporadas jugadas
            print(dt.obtener_mostrar_jugador_maximo(lista_jugadores, "temporadas"))

        case 20:    #Ingresar umbral y mostrar superadores de porcentaje de tiros de campo por posicion
            lista_superadores =dt.pedir_umbral_y_obtener_superadores(lista_jugadores, "porcentaje_tiros_de_campo") 
            dict_separacion_posicion = dt.separar_por_posicion(lista_superadores)

            for posicion,sublista in dict_separacion_posicion.items():
                print("--------------------------------\n{0}".format(posicion.upper()))
                dt.mostrar_todos_nombre_dato(sublista, "porcentaje_tiros_de_campo",sufijo='%')
            print("")

        case 21:
            break
        case 23:
            pass
        case _:
            print("Ingrese una opcion valida")
            pass

    input("Presione enter para continuar")
    os.system(clean_command)