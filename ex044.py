#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: -À vista dinheiro/cheque: 10% de desconto. -À vista no cartão: 5% de desconto. -Em até 2x no cartão: preço normal. -3x ou mais no cartão: 20% de juros.
p = float(input('PREÇO: R$'))
f = int(input("""ESCOLHA A FORMA DE PAGAMENTO:
[1] - À VISTA DINHEIRO/CHEQUE - 10% DE DESCONTO
[2] - À VISTA NO CARTÃO - 5% DE DESCONTO
[3] - 2X NO CARTÃO - 0% DE DESCONTO
[4] - 3X OU MAIS NO CARTÃO - 20 DE JUROS
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
:"""))
print('-=' * 20)
if f == 1:
	print(f"""À VISTA DINHEIRO/CHEQUE - 10% DE DESCONTO
PREÇO BASE - R${p:.2f} \nPREÇO A PAGAR - R${p / 100 * 90:.2f}""")
elif f == 2:
	print(f"""À VISTA NO CARTÃO - 5% DE DESCONTO
PREÇO BASE - R${p:.2f} \nPREÇO A PAGAR - R${p / 100 * 95:.2f}""")
elif f == 3:
	print(f"""2X NO CARTÃO - 0% DE DESCONTO
PREÇO BASE - R${p:.2f} \nPREÇO A PAGAR - R${p:.2f}""")
elif f == 4:
	print('3X OU MAIS NO CARTÃO - 20% DE JUROS')
	print('-=' * 20)
	q = int(input('QUANTAS PARCELAS? '))
	print('-=' * 20)
	print(f'PREÇO BASE - R${p:.2f} \nPREÇO COM JUROS - R${p / 100 * 120:.2f} \nVALOR DAS PARCELAS - {p / 100 * 120 / q:.2f}')
else:
	print('OPÇÃO INVÁLIDA')
print('-=' * 20)
