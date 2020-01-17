#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = list()
aluno = list()
opcao = 0
print(f'{"CADASTRO DE NOTAS":=^30}')

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(int(input('Nota 1:')))
    aluno.append(int(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    alunos.append(aluno[:])

    while True:
        continuar = str(input('Continuar? ')).strip().upper()

        if continuar != 'N' and continuar != 'S':
            print('=' * 15)
            print('OPÇÃO INVÁLIDA!')
            print('=' * 15)
        else:
            break

    if continuar == 'N':
        break

    aluno.clear()


while True:
    print('-' * 26)
    print(f'{"|cod=":=<10}{"Nome":=<10}{"Média"}|')

    for posicao, elemento in enumerate(alunos):
        print(f'|{posicao + 1:<9}{elemento[0]:<10}{elemento[2]:<5.2f}|')
    
    print('-' * 26)

    while True:
        opcao = int(input('Digite o cod: [999 p/ sair] '))

        if opcao > len(alunos) and opcao != 999:
            print('=' * 15)
            print('OPÇÃO INVÁLIDA!')
            print('=' * 15)
        
        elif opcao <= 0:
            print('=' * 15)
            print('OPÇÃO INVÁLIDA!')
            print('=' * 15)

        else:
            break
    
    if opcao == 999:
        break
    
    print('=' * 25)

    for elemento in alunos:
        if elemento == alunos[opcao - 1]:
            print(f'NOTAS DE {elemento[0].upper()}: {elemento[1]}, {elemento[2]}')

print('=' * 31)
input('pressione ENTER para sair')