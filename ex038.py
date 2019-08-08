#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: "0 primeiro valor é maior", "O segundo valor é maior" ou "Não existe valor maior, ambos são iguais." 
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número?: '))
print('-=' * 20)
if num1 > num2:
	print('O primeiro número é maior.')
elif num2 > num1:
	print('O segundo número é maior.')
else:
	print('Não existe maior ou menor.')
print('-=' * 20)
input('pressione ENTER para sair')