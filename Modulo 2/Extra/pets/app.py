from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['Nome']
        email = request.form['Email']
        mensagem = request.form['Mensagem']
    
        return f'Nome: {nome} | Email: {email} | Mensagem: {mensagem}'
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)