#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Salário: '))
if sal > 1250.00:
	print(f'O valor do aumento é de R${sal / 100 * 10}. \nO salário ficará R${sal / 100 * 110}')
else:
	print(f'O valor do aumento é de R${sal / 100 * 15}. \nO salário ficará R${sal / 100 * 115}')
print('-=' * 10)
input('pressione ENTER para sair')