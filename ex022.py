#ex022: Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas. Quantas letras ao todo(sem considerar espaços). Quantas letras tem o primeiro nome.
nome = str(input('Qual é o seu nome? ')).strip()
print(f'O seu nome completamente em minúsculo é: {nome.lower()}')
print(f'O seu nome completamente em maiúsculo é: {nome.upper()}')
print('O seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(dividido[0], len(dividido[0])))
print('-=' * 10)
input('pressione ENTER para sair')