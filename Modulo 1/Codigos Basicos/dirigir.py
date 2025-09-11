idade = int (input("Qual a sua idade?"))
CNH = input("Você possui habilitação? (s/n)")
print(f'pode dirigir? {CNH == 's' and idade >=18}')
