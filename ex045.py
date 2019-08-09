#Crie um programa que faça o computador jogar Jokenpô com você.
import time, random
esc = int(input("""JOKENPÔ! ESCOLHA:
[1] P/ PEDRA
[2] P/ PAPEL
[3] P/ TESOURA
: """))
print('-=' * 20)
maq = random.randint(1, 3)
print('J0...')
time.sleep(0.5)
print('KEN...')
time.sleep(0.5)
print('PÔ!')
time.sleep(0.5)
if esc == 1 and maq == 1:
	print("""PEDRA x PEDRA
EMPATOU!""")
elif esc == 1 and maq == 2:
	print("""PEDRA x PAPEL
VOCÊ PERDEU!""")
elif esc == 1 and maq == 3:
	print("""PEDRA x TESOURA
VOCÊ GANHOU!""")
elif esc == 2 and maq == 1:
	print("""PAPEL x PEDRA
VOCÊ GANHOU!""")
elif esc == 2 and maq == 2:
	print("""PAPEL x PAPEL
EMPATOU!""")
elif esc == 2 and maq == 3:
	print("""PAPEL x TESOURA
VOCÊ PERDEU!""")
elif esc == 3 and maq == 1:
	print("""TESOURA x PEDRA
VOCÊ PERDEU!""")
elif esc == 3 and maq == 2:
	print("""TESOURA x PAPEL
VOCÊ GANHOU!""")
elif esc == 3 and maq == 3:
	print("""TESOURA x TESOURA
EMPATOU!""")
else:
	print('OPÇÃO INVÁLIDA!')
print('-=' * 20)
input('pressione ENTER para sair')
