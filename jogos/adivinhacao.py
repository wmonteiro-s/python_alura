print("*"*33)
print("Bem vindo ao jogo de Adivinhação!")
print("*"*33)

numero_secreto = 42

chute = int(input("Digite um número: "))

print("\nVocê digitou", chute)

if numero_secreto == chute:
    print("\nParabéns, você acertou!")
else:
    print("\nQue pena, você errou.")

print("Fim do jogo!")