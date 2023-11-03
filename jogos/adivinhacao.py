print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

numero_secreto = 42

chute = int(input("Digite um número: "))

print("Você digitou", chute)

if numero_secreto == chute:
    print("\nParabéns, você acertou!")
else:
    print("\nQue pena, você errou.")

