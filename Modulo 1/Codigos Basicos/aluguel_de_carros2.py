modelo = (input('Qual foi o modelo do carro alugado?'))
dias = int (input('Por quantos dias o carro foi alugado?'))
km = float (input('Quantos km o carro rodou?'))

if modelo =='astra':
    diaria = 60
elif modelo == 'vectra':
    diaria = 50
elif modelo == 'golf':
    diaria = 70
else: 
    diaria = 40
    
total_dias = (dias*diaria)
total_km = (km*0.15)
valor_total = (dias+km)
print('Você alugou o carro por {dias} ')