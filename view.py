# SQLite
import sqlite3 as lite

# Conexão
conect = lite.connect('data.db')

# Inserir
def Inserir(i):
    with conect:
        cursor = conect.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES (?,?,?,?,?,?)"
        cursor.execute(query, i)

# Ler
def Ler():
    lista = []
    with conect:
        cursor = conect.cursor()
        query = "SELECT * FROM formulario"
        cursor.execute(query)
        info = cursor.fetchall()

        for i in info:
            lista.append(i)
        return lista

# Atualizar
def Atualizar(i):
    with conect:
        cursor = conect.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?,dia_em=?, estado=?, assunto=? WHERE id=?"
        cursor.execute(query, i)
'''
# Deletar
def Deletar():
    lista = [1]

    with conect:
        cursor = conect.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cursor.execute(query, lista)
'''