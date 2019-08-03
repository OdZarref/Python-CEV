#ex:020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
student1 = str(input('Primeiro Aluno: '))
student2 = str(input('Segundo Aluno: '))
student3 = str(input('Terceiro Aluno: '))
student4 = str(input('Quarto aluno: '))
list = [student1, student2, student3, student4]
shuffle(list)
print(f'A ordem escolhida é: {list}')
print('-=' * 10)
input('pressione ENTER para sair')
