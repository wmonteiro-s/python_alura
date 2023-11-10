print("*"*33)
print("Bem vindo ao jogo de Adivinhação!")
print("*"*33)

numero_secreto = 42

chute = int(input("Digite um número: "))

print("\nVocê digitou", chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print("\nParabéns, você acertou!")
else:
    if maior:
        print("\nQue pena, você errou. O seu chute foi MAIOR que o número secreto")
    elif menor:
        print("\nQue pena, você errou. O seu chute foi MENOR que o número secreto")

print("Fim do jogo!")