def intercalar_listas(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i])
        resultado.append(lista2[i])
    return resultado
print(intercalar_listas([1, 2, 3], ["a", "b", "c"]))