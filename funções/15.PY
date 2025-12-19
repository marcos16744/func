def analisa_lista(lista):
    if not lista:
        return None, None, None  
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    return maior, menor, media
resultado = analisa_lista([10, 5, 8, 20, 3])
print(resultado)