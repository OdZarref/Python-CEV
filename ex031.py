#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço  da passagem, cobrando R$0.50 por KM para viagens de até 200KM e R$0.45 para viagens mais longas.
dis = int(input('Distância em KM: '))
if dis <= 200:
	print(f'Esta viagem vai custar R${dis * 0.50}')
else:
	print(f'Esta viagem vai custar R${dis * 0.45}')
print('-=' * 10)
input('pressione ENTER para sair')