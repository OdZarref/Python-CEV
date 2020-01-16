#Crie um programa  onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print(f'{"ANALISADOR DE EXPRESSÕES":=^40}')
expressao = str(input('Expressão: '))
pilha = []
print('=' * 25)

for caractere in expressao:
	if '(' in caractere:
		pilha.append('(')

	elif ')' in caractere:
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')

if len(pilha) == 0:
	print('Expressão correta!')
else:
	print('Expressão incorreta!')

print('=' * 25)
input('pressione ENTER para sair')