#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, que agora utilizando um laço for.
tabuada = int(input('Tabuada: '))
for c in range(1, 11):
	print(f'{tabuada} x {c:2} = {tabuada * c}')
print('-=' * 10)
input('pressione ENTER para sair')