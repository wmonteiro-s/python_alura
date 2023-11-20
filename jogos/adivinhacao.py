import random

print("*"*33)
print("Bem vindo ao jogo de Adivinhação!")
print("*"*33, "\n")

numero_secreto = random.randrange(1,101)
tentativas = 1
max_tentativas = 0
pontos = 1000
print(numero_secreto)

print("\nEscolha o nível de dificuldade\n(1)Fácil | (2)Médio | (3)Difícil")

while True:
    nivel = int(input("\nSelecione um dos níveis indicados: "))

    if nivel == 1:
        print("<-Nível Fácil->\n")
        max_tentativas = 20
        break
    elif nivel == 2:
        print("<-Nível Médio->\n")
        max_tentativas = 10
        break
    elif nivel == 3:
        print("<-Nível Difícil->\n")
        max_tentativas = 5
        break
    else:
        print("***Este não é um nível selecionável***")
        continue
    
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
        print(f'Parabéns, você acertou e fez {pontos} pontos!\n')
        break
    elif maior:
        print("Que pena, você errou. O seu chute foi MAIOR que o número secreto\n")
    elif menor:
        print("Que pena, você errou. O seu chute foi MENOR que o número secreto\n")
    else:
        print("Não é válido\n")

    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

print("Fim do jogo!")