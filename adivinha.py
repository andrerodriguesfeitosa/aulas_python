import random
import os

#defina os valores
numero_inicial = 1
numero_final = 100
max_tentativas = 6

numero_secreto = random.randint(numero_inicial,numero_final)
tentativas = 0
acertou = False

print('+++++ Bem vindo ao Python Games +++++')
print(f'Você possui {max_tentativas} tentativas para adivinhar o número secreto entre {numero_inicial} e {numero_final}')

while tentativas < max_tentativas:
    palpite = int(input(f'Digite um número inteiro entre {numero_inicial} e {numero_final}, Você ainda tem {max_tentativas - tentativas} tentativas. '))
    tentativas += 1 

    if palpite == numero_secreto:
        acertou = True
        break

    elif palpite < numero_secreto:
        os.system('cls')
        print('Tente um número maior!')
    
    else:
        os.system('cls')
        print('Tente um número menor!')


if acertou:
    os.system('cls')
    print(f'Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.')
else:
    os.system('cls')
    print(f'Que pena! Você não conseguiu adivinhar o número secreto: {numero_secreto}')