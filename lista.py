#lista
lista_nomes = ['gomes', 'oliveira', 'lucas', 'jose', 'pedro', 'maria', 'lucas', 'joao']

for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista é: {lista_nomes[i]}')

novo_nome = input('Digite o novo nome que será adicionado na lista: ')

posicao = input('Digite a posição que deseja colocar esse nome: ')
posicao = int(posicao)

#corrigindo a posição
posicao -= 1

if posicao >= 0 and posicao <= len(lista_nomes):
    lista_nomes.insert(posicao, novo_nome)
else:
    print('Posilção inválida!')


#exibindo a lista atualizada
print()
print(30*'=', 'lista atualizada', 30*'=')

for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista é: {lista_nomes[i]}')