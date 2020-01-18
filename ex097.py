#Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. ex) escreva('Olá, mundo!') saída) -----------\nOlá, mundo!\n-----------
def escreve(mensagem):
    print(mensagem)
    print('~' * len(mensagem))


mensagem = "Take me out tonight"
escreve(mensagem)
mensagem = "Where there's music"
escreve(mensagem)
mensagem = "and there's people"
escreve(mensagem)
mensagem = "and they're young and alive"
escreve(mensagem)

input('pressione ENTER para sair')
