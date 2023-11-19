import random


print("*"*33)
print("Bem vindo ao jogo de Adivinhação!")
print("*"*33, "\n")

numero_secreto = round(random.random() * 100)
tentativas = 1
max_tentativas = 5
print(numero_secreto)

for tentativas in range(tentativas, max_tentativas + 1):
    print(f'Tentativa {tentativas} de {max_tentativas}')
    chute = int(input("Digite um número entre 1 e 100: "))
    print(f'Você digitou {chute}')

    if chute < 1 or chute > 100:
        print("O número digitado deve estar entre 1 e 100\n")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabéns, você acertou!\n")
        break
    elif maior:
        print("Que pena, você errou. O seu chute foi MAIOR que o número secreto\n")
    elif menor:
        print("Que pena, você errou. O seu chute foi MENOR que o número secreto\n")
    else:
        print("Não é válido\n")

print("Fim do jogo!")