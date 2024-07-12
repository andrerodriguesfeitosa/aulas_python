import os
import time

lista_cpf = ['12345678', '2345678', '987654321']
lista_usuarios = ['gomes', 'oliveira', 'lucas']

os.system('cls')
while True:
    print(30*'-', 'Bem vindo ao sistema Python cadastros' ,30*'-')
    print('1. Cadastrar usuário')
    print('2. Consultar usuário')
    print('3. Acessar o sistema')
    print('4. Remover um usuario')
    print('5. Sair')

    opcao = input('Digite a opção desejada: ')

    #cadastrar
    if opcao == '1':

        os.system('cls')
        novo_nome = input('Digite o nome: ')
        novo_cpf = input('Digite o cpf: ')

        if novo_cpf in lista_cpf:
            print('O cpf ja existe!')
        else:
            lista_cpf.append(novo_cpf)
            lista_usuarios.append(novo_nome)
            print('Usuário cadastrado com sucesso!')

    # consultar usuarios
    elif opcao == '2':

        os.system('cls')
        for i in lista_usuarios:
            print(f'Usuário {i}')

    # acessar sistema
    elif opcao == '3':

        os.system('cls')
        cpf_login = input('Digite o CPF: ')
    
        if cpf_login in lista_cpf:
            print('Acesso realizado com sucesso!')
        else:
            print('Usuário não possui cadastro!')
    
    elif opcao == '4':

        os.system('cls')
        cpf_remove = input('Digite o CPF a ser removido: ')
        
        if cpf_remove in lista_cpf:
            indice = lista_cpf.index(cpf_remove)
            nome = lista_usuarios.pop(indice)
            lista_cpf.pop(indice)

            print(f'Usuário: {nome} com CPF {cpf_remove} foi removido com sucesso!')
    
    elif opcao == '5':

        os.system('cls')
        print('Saindo do sistema')
        time.sleep(3)
        break

    else:

        os.system('cls')
        print('Opção inválida!')
