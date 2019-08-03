#ex004: Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
num = str(input('Digite algo: '))
#Verá se é numérico
print('É numérico? ', end='')
print(num.isnumeric())
#Verá se é alfabético
print('É alfabético? ', end='')
print(num.isalpha())
#Verá se é alfanumérico
print('É alfanumérico? ', end='')
print(num.isalnum())
#Verá se está totalmente em maiúsculo
print('Está totalmente em maiúsculo? ', end='')
print(num.isupper())
print('-=' * 10)
input('pressione ENTER para sair')
