#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
import ex108moedas

preco = float(input('Preço: '))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_diminuicao = int(input('Porcentagem de diminuição: '))

print('=' * 40)
print(f'Com o aumento de {porcentagem_aumento}% o preço fica R${ex108moedas.aumentar(preco, porcentagem_aumento)}')
print(f'Com a diminuição de {porcentagem_diminuicao}% o preço fica R${ex108moedas.diminuir(preco, porcentagem_diminuicao)}')
print(f'A metade é R${ex108moedas.metade(preco)}')
print(f'O dobro é R${ex108moedas.dobro(preco)}')
print('=' * 40)

input('pressione ENTER para sair')