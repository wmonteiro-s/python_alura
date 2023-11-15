print("*"*33)
print("Bem vindo ao jogo de Adivinhação!")
print("*"*33, "\n")

numero_secreto = 42
tentativas = 1

while tentativas <= 3:
    print(f'Tentativa {tentativas} de 3')
    chute = int(input("Digite um número: "))

    print("Você digitou", chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabéns, você acertou!\n")
    elif maior:
        print("Que pena, você errou. O seu chute foi MAIOR que o número secreto\n")
    elif menor:
        print("Que pena, você errou. O seu chute foi MENOR que o número secreto\n")
    else:
        print("Não é válido\n")

    tentativas += 1

print("Fim do jogo!")