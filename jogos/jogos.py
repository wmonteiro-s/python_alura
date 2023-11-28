import forca
import adivinhacao

while True:
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca | (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

    saida = input("Você deseja continuar jogando? [S]Sim [N]Não: ").upper()
    if saida.strip() == saida.strip("S") or saida.strip() == saida.strip("SIM"):
        break
    elif saida.strip() == saida.strip("N") or saida.strip() == saida.strip("NÃO") or saida.strip() == saida.strip("NAO"):
        continue