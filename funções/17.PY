import random

def simular_dado(n):
    resultados = []
    for _ in range(n):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados
print(simular_dado(5))