from colorama import init, Fore
init(autoreset=True)



print('|--------------------|')
print('|    CALCULADORA     |')
print('|--------------------|')
print('| 01- Soma           |')
print('| 02- Subtração      |')
print('| 03- Multiplicação  |')
print('| 04- Divisão        |')
print('----------------------')
opcoes = int(input('Escolha uma das opções: '))
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if opcoes == 1:
    print(numero1+numero2)
elif opcoes == 2:
    print(numero1-numero2)
elif opcoes == 3:
    print(numero1*numero2)
elif opcoes == 4:
    print(numero1/numero2)
else:
    print('ERRO!, Digite uma opção válida!')