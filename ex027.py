#ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza primeiro = Ana último = Souza
name = str(input('Digite o seu nome completo: ')).split()
print('O seu primeiro nome é {}. O seu último nome é {}.'.format(name[0], name[len(name) - 1]))
print('-=' * 10)
input('pressione ENTER para sair')