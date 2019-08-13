#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

maiores = menores = 0
atual = datetime.date.today().year

for c in range(1, 8):
	datanas = int(input(f'DATA DE NASCIMENTO DA {c}º PESSOA: '))
	if atual - datanas >= 21:
		maiores += 1
	else:
		menores += 1

print('-=' * 29)
print(f'A QUANTIDADE DE MAIORES É {maiores}. E A QUANTIDADE DE MENORES É {menores}.')
print('-=' * 29)
input('pressione ENTER para sair')