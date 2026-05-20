"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    valores = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            cols = line.split("\t")
            letra = cols[0]
            valor = int(cols[1])
            if letra not in valores:
                valores[letra] = [valor, valor]
            else:
                if valor > valores[letra][0]:
                    valores[letra][0] = valor
                if valor < valores[letra][1]:
                    valores[letra][1] = valor
    return [(k, v[0], v[1]) for k, v in sorted(valores.items())]

print(pregunta_05())
"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
