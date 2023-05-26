import parcial_biblioteca as dt

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
        " "]

    print("{0}".format("{0} - {1}".format(i, lista_opciones[i] for i in range(len(lista_opciones)))))

    input = dt.pedir_entero(mensaje_input = "Ingrese una opcion: ")
    
    print( input in range(20))
        