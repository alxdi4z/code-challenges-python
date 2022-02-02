from pprint import pprint

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]


def rotateMatrix(a: list) -> list:
    # a = list(zip(*a))
    # a = [list(l[::-1]) for l in a]
    # return a

    # em zip(*lista) o * indica que queremos desempacotar a lista de argumento
    # tornando cada elemento em um argumento separado
    z = zip(*a)
    a = list(z)
    print(f"Lista depois do zip: {a}")
    lista_retorno = []
    for tupla in a:
        # criando uma lista de cada tupla e invertendo seus elementos
        lista = list(tupla[::-1])
        lista_retorno.append(lista)

    return lista_retorno


pprint(rotateMatrix(arr))
