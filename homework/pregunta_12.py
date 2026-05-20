"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    sumas = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letra = cols[0]
            col5 = cols[4]
            total = sum(int(par.split(":")[1]) for par in col5.split(","))
            sumas[letra] = sumas.get(letra, 0) + total
    return dict(sorted(sumas.items()))

print(pregunta_12())
"""
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
