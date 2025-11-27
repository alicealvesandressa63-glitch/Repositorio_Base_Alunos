import sqlite3

nome = input('Digite o seu nome: ')
email = input('Digite seu email: ')
idade = input('Digite sua idade: ')
usuario = input('Crie um nome de usuário:')
senha = input('Crie uma senha forte: ')


script_cadastro = """CREATE TABLE IF NOT EXISTS Cadastro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                idade INTEGER NOT NULL,
                usuario TEXT NOT NULL,
                senha TEXTE NOT NULL
            );"""

banco = 'cadastro.db'

try:
    with sqlite3.connect(banco) as conn:
        # Cria um cursor
        cur = conn.cursor()

        # Executa o script
        cur.execute(script_cadastro)

        # Salva as alterações no banco de dados
        conn.commit()

        print("Tabelas Criadas com Sucesso")
except sqlite3.OperationalError as e:
    print("ERRO: ", e)


sql = "INSERT INTO Cadastro (nome, email, idade, usuario, senha) VALUES (?,?,?,?,?)"

try:
    with sqlite3.connect(banco) as conn:
            
        # Cria um cursor
        cur = conn.cursor()

        # Executa o script
        cur.execute(sql, (nome, email, idade, usuario, senha))

        # Salva as alterações no banco de dados
        conn.commit()

except sqlite3.OperationalError as e:
    print("ERRO: ", e)
        