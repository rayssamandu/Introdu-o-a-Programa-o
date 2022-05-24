import random

print('''
    BEM VINDO (A) AO JOGO DA FORCA !
    O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui. 
    A cada rodada, os jogadores irão simultaneamente escolher uma letra que suspeitem fazer parte da palavra. 
    Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está. Ao contrário, o jogador será enforcado.
    Você tem 6 chances.
    BOA SORTE !
==== MENU: ====
[1] - Alimentos
[2] - Lugares
[3] - Objetos
''')
alimentos = ['JABOTICABA', 'PINHA', 'MELANCIA', 'MANGA', 'GOIABA']
lugares = ['GRAMADO', 'PARATI', 'SALVADOR', 'BANANEIRAS', 'MEXICO']
objetos = ['TECLADO', 'POLTRONA', 'QUADRO', 'TAPETE', 'TALHER']
digitadas = []
acertos = []
erros = 0

valid_usuario = False

while valid_usuario == False:
    usuario = input('DIGITE A OPÇÃO DESEJADA: ').lower()
    if usuario == "a":
        palavra = random.choice(alimentos)
        break
    elif usuario == "l":
        palavra = random.choice(lugares)
        break
    elif usuario == "o":
        palavra = random.choice(objetos)
        break
    else:
        valid_usuario = True
        print("A categoria escolhida não é válida, por favor, selecione uma das opções do Menu!")


while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        break
