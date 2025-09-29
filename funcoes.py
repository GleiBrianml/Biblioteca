import sqlite3
def cadastrar_livro(titulo,autor,ano):
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO Biblioteca (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, "Sim"))
    conexao.commit()
    conexao.close()
def listar_livro():
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Biblioteca")
#fetchall traz todas as linhas da consulta
    for linha in cursor.fetchall(): return(f"ID {linha[0]}| Título: {linha[1]} | Ano: {linha[2]} | Autor: {linha[3]} | Disponivel : {linha[4]}")

