def jogar():
    print("*"*27)
    print("Bem vindo ao jogo da Forca!")
    print("*"*27, "\n")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual letra? ").strip()

        index = 1
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f'A letra "{letra}" é a {index}ª letra na palavra {palavra_secreta}')

            index += 1
        print("Jogando...")

    print("Fim do jogo!")
if __name__ == "__main__":
    jogar()