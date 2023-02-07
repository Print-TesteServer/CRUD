# SQLite
import sqlite3 as lite

# Conexão
conect = lite.connect('data.db')

# Inserir
lista = [ 'Joao Futi Muanda', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']

with conect:
    cursor = conect.cursor()
    query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES (?,?,?,?,?,?)"
    cursor.execute(query, lista)

# Ler
with conect:
    cursor = conect.cursor()
    query = "SELECT * FROM formulario"
    cursor.execute(query)
    info = cursor.fetchall()
    print(info)

# Atualizar
lista = ['João', 1]

with conect:
    cursor = conect.cursor()
    query = "UPDATE formulario SET nome=? WHERE id=?"
    cursor.execute(query, lista)

# Deletar
lista = [1]

with conect:
    cursor = conect.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cursor.execute(query, lista)