import sqlite3
# def criar_pasta():
    

    #cria uma conexão com o banco de dados chamado "escola.db"
conexao = sqlite3.connect("Biblioteca.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

#Ciar uma tabela no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS Biblioteca(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    título TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTERGER,
    disponivel TEXT)
    """)
print("Tabela criada com sucesso!")