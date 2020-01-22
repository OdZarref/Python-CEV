#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from libs.interface import *
from libs.arquivo import *

arquivo_pessoas = 'pessoas_dados'

if not existencia_arquivo(arquivo_pessoas):
    criar_arquivo(arquivo_pessoas)

while True:
    linhas('MENU')
    mostrar_opcoes(['Cadastrar', 'Mostrar Cadastrados', 'Sair'])

    linhas('DIGITE A SUA OPÇÃO')
    escolha = leia_inteiro('>> ')

    if escolha == 1:
        linhas('NOVO CADASTRO')
        nome_pessoa = str(input('Nome: '))
        idade_pessoa = leia_inteiro('Idade: ')

        cadastrar(arquivo_pessoas, nome_pessoa, idade_pessoa)

    elif escolha == 2:
        linhas('PESSOAS CADASTRADAS')
        ler_arquivo(arquivo_pessoas)
    
    elif escolha == 3:
        print('PROGRAMA FINALIZADO.')
        break

    else:
        print('=' * 30)
        print('\033[31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
    