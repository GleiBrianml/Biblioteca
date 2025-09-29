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
    for linha in cursor.fetchall(): 
        return(f"ID {linha[0]}| Título: {linha[1]} | Ano: {linha[2]} | Autor: {linha[3]} | Disponivel : {linha[4]}")

def updade_dispo(id_livro):
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT disponivel FROM Biblioteca WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if resultado:
        status_atual = resultado[0]

        if status_atual.lower() == "sim":
            novo_status = "Não"
        else:
            novo_status = "Sim"

        cursor.execute("""
            UPDATE Biblioteca
            SET disponivel = ?
            WHERE id = ?
        """, (novo_status, id_livro))

        conexao.commit()
        print(f"Status atualizado para '{novo_status}'.")
    else:
        print("Livro com o ID informado não encontrado.")

    conexao.close()

    