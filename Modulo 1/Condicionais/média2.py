print("------------------------------")
print("|    SISTEMA DE PROVAS       |")
print("------------------------------")
nome = input("Nome do aluno:")
prova1 = float(input("Nota da primeira prova:"))
prova2 = float(input("Nota da segunda prova:"))
prova3 = float(input("Nota da terceira prova:"))
media = prova1+prova2+prova3/3
if media >=5:
    print('aprovado')
elif media ==5:
    print('recuperação')
else:
    print('reprovado')
print("------------------------------")