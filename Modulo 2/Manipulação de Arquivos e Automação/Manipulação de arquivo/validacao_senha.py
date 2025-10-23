import json

with open('senha.json', 'r', encoding = 'utf-8') as arquivo:
    dados = json.load(arquivo)

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')

if email == dados['Email'] and senha == dados['Senha']:
    print('Acesso liberado!')
else:
    print('Acesso negado! ')