# sorteio
import random
import os

lista = []
lista_sorteados = []

while True:
    nome = input('Digite os nomes que serão sorteados: ')

    if nome != '':
        lista.append(nome) 
    else:
        break

lista_temp = lista.copy()

while True:
    if lista_temp:
        os.system('cls')   
        premiado = random.choice(lista_temp)
        lista_temp.remove(premiado)
        lista_sorteados.append(premiado)

        print(f'O premiado da vez é o {premiado}')
        
        opcao = input('Deseja realizar um novo sorteio? (s/n)').lower()
        os.system('cls')

        if opcao != 's':
            break

    else:
        print('Não existem nomes para ser sorteados!')
        break

print('Sistema Finalizado')
print('Participantes: ',lista)
print('Sorteados: ',lista_sorteados)

