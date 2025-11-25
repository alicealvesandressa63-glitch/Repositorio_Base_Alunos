# Exercicio 2-2: Links entre rotas
# Adicione um menu de navegação simples com links para todas as suas rotas (/, /sobre, /saudacao, etc.).
# Passar a variável através do 'url_for' dentro do script html: ("{{ url_for('saudacao', nome='João') }}")
# 'saudacao' é o nome da função Python que define a rota.
# nome='João' está passando o valor para a variável que a rota espera (<nome>).

from flask import Flask, render_template 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return f'Olá, tudo bem? Me chamo Alice e sou uma estudante de Python, espero poder me aprofundar mais e atuar nessa área em breve.'

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