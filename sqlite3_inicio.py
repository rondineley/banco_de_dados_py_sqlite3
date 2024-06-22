import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco_de_dados.sqlite")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
       "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

def inserir_registro(conexao, cursor, nome, gmail):
    data = (nome, gmail)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, gmail, id):
    data = (nome, gmail, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados): 
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()

def lista_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

dados = [
    ("Pedro Ricardo", "pedro123@gmail.com"), 
    ("Rosa Helena", "rosa123@gmail.com"), 
    ("Rondiney", "rondiney123@gmail.com")
    ]

clientes = lista_clientes(cursor)
for cliente in clientes:
    print(cliente)

#inserir_registro(conexao, cursor, "Pedro Ricardo", "xtx2724@gmail.com")

#inserir_muitos(conexao, cursor, dados)

#atualizar_registro(conexao, cursor, "Pedro Ricardo", "xtx2724@gmail.com", 3)

#excluir_registro(conexao, cursor, 2)

print(lista_clientes)

conexao.close()
