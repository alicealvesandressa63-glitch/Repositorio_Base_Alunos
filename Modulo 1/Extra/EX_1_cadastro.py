# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|--------------------|')
print('|     CADASTRO       |')
print('|--------------------|')
nome = input('Nome: ')
idade = input('Idade: ')
email = input('Email: ')
senha = input('Senha: ')

print('|--------------------|')
print('| USUÁRIO CADASTRADO |')
print('|--------------------|')
print('Seja bem vindo(a)',nome,)
print('email:',email)