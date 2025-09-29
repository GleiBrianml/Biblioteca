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

