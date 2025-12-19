def contar_vogais(palavra):
    vogais = 'aeiou'
    palavra = palavra.lower()
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
print(contar_vogais("python"))  