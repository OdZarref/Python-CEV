#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
print(f'{"ORGANIZADOR":=^19}')
lista = [[], []]

for contador in range(0, 7):
    dado = int(input(f'Digite {contador + 1}° número: '))

    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        lista[1].append(dado)

lista[0].sort()
lista[1].sort()

print('=' * (24 + len(str(lista[1]))))
print(f'Os valores ímpares são: {lista[1]}')
print(f'Os valores pares são: {lista[0]}')
print('=' * 25)
input('pressione ENTER para sair')