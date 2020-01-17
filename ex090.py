#Faça um programa que leia nome e média de um aluno, guardando tambéma situação em um dicionário. No final mestre o conteúdo da estrutura na tela.
print(f'{"CONSULTA ESCOLA":=^35}')
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] < 5:
    aluno['situacao'] = 'reprovado'.upper()

elif aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'.upper()

else:
    aluno['situacao'] = 'recuperação'.upper()

print('=' * 35)
print(f'A situação do {aluno["nome"]} é {aluno["situacao"]}')
print('=' * 35)
input('pressione ENTER para sair')
