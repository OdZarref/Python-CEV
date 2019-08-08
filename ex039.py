#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar. -Se é a hora de alistar. -Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
datanas = int(input('Digite o seu ano de nascimento: ')) #Ano de nascimento
datahj = datetime.date.today().year #Ano atual
print('-=' * 20)
if datahj - datanas < 18:
	print(f'Você ainda irá se alistar. Faltam {18 - (datahj - datanas)} ano(s) para o seu alistamento.')
elif datahj - datanas == 18:
	print('Você deve ser apresentar para o alistamente de imediato.')
else:
	print(f'Você deveria ter se alistado em {datanas + 18}.')
print('-=' * 20)
input('pressione ENTER para sair')
