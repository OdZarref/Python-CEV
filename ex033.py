#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = menor = num1
#maior
if num2 > num1 and num2 > num3:
	maior = num2
elif num3 > num1 and num3 > num2:
	maior = num3
#menor
if num2 < num1 and num2 < num3:
	menor = num2
elif num3 < num1 and num3 < num2:
	menor = num3
print(f'O menor número é {menor} e o maior número é {maior}.')