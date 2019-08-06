#ex025: Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.
name = str(input('Qual o seu nome completo? ')).strip().upper()
print('Você tem silva no nome? {}'.format('SILVA' in name))
print('-=' * 10)
input('pressione ENTER para sair')
