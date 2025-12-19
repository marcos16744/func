def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(fatorial(5))