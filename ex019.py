#ex019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

name1 = str(input('DIGITE O PRIMEIRO NOME: '))
name2 = str(input('DIGITE O SEGUNDO NOME: '))
name3 = str(input('DIGITE O TERCEIRO NOME: '))
name4 = str(input('DIGITE O QUARTO NOME: '))
list = [name1, name2, name3, name4]
choice = random.choice(list)
print(f'O escolhido é {choice}')
print('-=' * 10)
input('pressione enter para sair')
