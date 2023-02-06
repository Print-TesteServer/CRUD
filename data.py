# Banco de dados - SQLite
import sqlite3 as lite

# Conexão
conect = lite.connect('data.db')

# Tabela
with conect:
    cursor = conect.cursor()
    cursor.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCOREMENT,"
                    "nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT) ")