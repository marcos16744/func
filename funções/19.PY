def jogo_adivinhacao(numero_secreto):
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
        
        if palpite > numero_secreto:
            print("Maior que o número secreto")
        elif palpite < numero_secreto:
            print("Menor que o número secreto")
        else:
            print("Parabéns! Você acertou!")
            break
jogo_adivinhacao(42)
      
