#Faça um programa que tenha um função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: -Quantidade de notas -A maior nota -A menor nota -A média da turma -A situação (opcional)


def notas(*notas, situacao=False):
    """    Função notas(): Analisa várias notas, dá uma média e situação (se for pedido).
    Parâmetro notas: Parâmetro para as notas.
    Parâmetro situacao: Parâmetro lógico para mostrar a situação da sala.
    return: Um dicionário com as informações da sala.
    """
    ficha_sala = dict()
    ficha_sala['quantas_notas'] = len(notas)
    ficha_sala['maior_nota'] = max(notas)
    ficha_sala['menor_nota'] = min(notas)
    ficha_sala['media'] = sum(notas) / len(notas)

    if situacao == True:
        if ficha_sala['media'] < 5:
            ficha_sala['Situação'] = 'RUIM'

        elif ficha_sala['media'] > 7:
            ficha_sala['Situação'] = 'Excelente'

        else:
            ficha_sala['Situação'] = 'RAZOÁVEL'
    
    return ficha_sala


resposta = notas(6, 7, 10, 5, 7, 10, situacao=True)
print(resposta)
print(notas.__doc__)
