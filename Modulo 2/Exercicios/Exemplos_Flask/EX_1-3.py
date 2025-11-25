# EXERCICIO 1-3: Parâmetros na URL (rotas dinâmicas)
# Crie uma rota /saudacao/<nome> que retorna "Olá, <nome>! Seja bem-vindo!".
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


if __name__ == '__main__':
    app.run(debug=True)