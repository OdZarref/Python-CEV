#ex026: Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra ‘A’ Em que posição ela aparece a primeira vez Em que posição ela aparece a última vez
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A letra "A" aparece {} vezes. Pela primeira vez na posição {}. E pela última vez na posição {}'.format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))
print('-=' * 10)
input('pressione ENTER para sair')
