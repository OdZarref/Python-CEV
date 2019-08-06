#ex029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.
vel = int(input('Velocidade: '))
if vel > 80:
	print(f'Você foi multado por excesso de velocidade! O valor da multa é R${(vel - 80) * 7}.')
else:
	print('Tudo nos conformes. Tenha uma boa viagem!')
print('-=' * 10)
input('pressione ENTER para sair')