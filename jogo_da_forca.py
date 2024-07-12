import random
import os

lista_palavras = ['python', 'programação', 'computador', 'notebook', 'software', 'openai']

palavra = random.choice(lista_palavras)
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    palavra_escondida = ''
    for letra in  palavra:
        if letra in letras_corretas:
            palavra_escondida += letra
        else:
            palavra_escondida += '_ '
    
    os.system('cls')

    print()
    if tentativas or tentativas == 0:
        print(19*'='+'|')
        print(19*' '+'|')

    if tentativas <= 5 and tentativas != 0:
        print(16*' '+'[o _ 0]')
        print(18*' '+'| |')

    if tentativas == 0:
        print(16*' '+'[x _ x]')
        print(18*' '+'| |')

    if tentativas == 4:
        print(14*' '+'===========')
        print(14*' '+'   =====   ')
        print(14*' '+'   =====   ')
        print(14*' '+'   =====   ')
        print(13*' '+'    =====   ')            

    if tentativas == 3:
        print(14*' '+'===========')
        print(14*' '+'   =====  =')
        print(14*' '+'   =====  =')
        print(14*' '+'   =====  =')
        print(13*' '+'    =====  ||')            

    if tentativas == 2 or tentativas == 1 or tentativas == 0:
        print(14*' '+'===========')
        print(14*' '+'=  =====  =')
        print(14*' '+'=  =====  =')
        print(14*' '+'=  =====  =')
        print(13*' '+'||  =====  ||')            

    if tentativas == 1:
        print(14*' '+'       =   ')
        print(14*' '+'       =   ')
        print(14*' '+'       =   ')
        print(14*' '+'       ==  ')

    if tentativas == 0:
        print(14*' '+'   =   =   ')
        print(14*' '+'   =   =   ')
        print(14*' '+'   =   =   ')
        print(14*' '+'  ==   ==  ')

        print()    

    print('Palavra:', palavra_escondida)
    print('Letras erradas:', letras_erradas)
    print('Tentativas restantes:', tentativas)

    if palavra_escondida == palavra:
        print('Você acertou!')
        break
    elif tentativas == 0:
        print('Você perdeu! a palavra era:', palavra)
        break
    
    letra_usuario = input('Digite uma letra: ').lower()

    if letra_usuario in palavra:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        print('Letra errada!')
        letras_erradas.append(letra_usuario)
        tentativas -= 1