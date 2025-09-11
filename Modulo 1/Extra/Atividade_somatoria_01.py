print('|----------------------|')
print('|Monitoramento de Saúde|')
print('|----------------------|')
nome = input('| Digite seu nome: ')
peso = float (input('| Digite o seu peso: '))
altura = float (input('| Digite a sua altura: '))
imc = peso / (altura ** 2)
if imc <18.5:
    print('Abaixo do peso, procure um especialista')
elif imc <=24.9:
    print('Peso normal, tudo ok.')
elif imc <=29.9:
    print('Começo de sobrepeso, procure um especialista se for necessário. ')
elif imc<=34.9:
    print('Obesidade Grau 1, procure ajuda de um especialista.')
elif imc<=39.9:
    print('Obesidade Grau 2, procure ajuda de um especialista.')
else:
    print('Obesidade Grau 3, procure ajuda de um especialista.')