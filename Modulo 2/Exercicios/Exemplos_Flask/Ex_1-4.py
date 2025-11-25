# EXERCICIO 1-4: Rota com número (tipagem na rota)
# Crie uma rota /dobro/<int:numero> que recebe um número e retorna o dobro dele.
from flask import Flask 


app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo!'

@app.route('/sobre')
def sobre():
    return 'Oie, tudo bem? Me chamo Alice e sou estudante do curso de Python.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    if nome == 'Alice':
        return f'Olá Mestra. Seja bem-vinda de volta!'
    else:
        return f'Olá, {nome}! Seja bem-vindo espero que aproveite. '
    
@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O  dobro de {numero} será {numero*2}'


if __name__ == '__main__':
    app.run(debug=True)