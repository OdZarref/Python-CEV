def existencia_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print('ERRO AO CRIAR ARQUIVO!')


def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except:
        print('ERRO AO LER ARQUIVO')
    else:
        print(arquivo.read())


def cadastrar(nome_arquivo, nome='desconhecido', idade=18):
    try:
        arquivo = open(nome_arquivo, 'at')
    except:
        print('ERRO AO ABRIR ARQUIVO')
    else:
        try:
            arquivo.write(f'{nome}; {idade}\n')
        except:
            print('ERRO AO ESCREVER ARQUIVO')
        else:
            print(f'{nome} adicionado com sucesso!')
