#Crie um código em Python que teste se o site Pudim está acessível no computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não é acessível no momento.')
else:
    print('O site está acessível')
