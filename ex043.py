#Desenvolva uma lógica que leia o peso a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
#-Abaixo de 18.5: Abaixo do peso. -Entre 18.5 e 25: Peso ideal. -25 até 30: Sobrepeso. -30 até 40: Obesidade. -Acima de 40: Obesidade mórbida.
peso = float(input('PESO: (KILOS)'))
alt = float(input('ALTURA: (METROS)'))
imc = peso / alt ** 2
print('-=' * 20)
if imc < 18.5:
	print(f'O seu IMC é {imc:.1f}, você está ABAIXO DO PESO.')
elif imc <= 25:
	print(f'O seu IMC é {imc:.1f}, você está no PESO IDEAL.')
elif imc <= 30:
	print(f'O seu IMC é {imc:.1f}, você está no SOBREPESO.')
elif imc <= 40:
	print(f'O seu IMC é {imc:.1f}, você está em OBESIDADE.')
elif imc > 40:
	print(f'O seu IMC é {imc:.1f}, você está em OBESIDADE MÓRBIDA.')
print('-=' * 20)
input('pressione ENTER para sair')
