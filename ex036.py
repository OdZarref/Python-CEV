#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sendo que ela não vai exceder 30% do salário ou então o empréstimo será negado.
cs = float(input('Qual o valor da casa? R$')) #casa
sal = float(input('Qual o seu salário? R$')) #salário
anos = int(input('Em quantos anos você irá parcelar? ')) #anos
pres = cs / (anos * 12) #prestação
print('-=' * 20)
if pres > sal / 100 * 30:
	print('<EMPRÉSTIMO NEGADO> \nO valor da prestação ultrapassa 30% do seu salário.')
else:
	print('<EMPRÉSTIMO APROVADO!> \nAs parcelas serão de R${:.2f} por um período de {} meses.'.format(pres, anos * 12))
print('-=' * 20)
input('pressione ENTER para sair')