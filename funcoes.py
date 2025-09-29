import sqlite3
def cadastrar_livro():
    titulo = input("Digite o titulo do livro que deseja cadastrar: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Insirar o ano do livro: "))
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
        print(f"ID: {linha[0]}| Título: {linha[1]} | Ano: {linha[2]} | Autor: {linha[3]} | Disponivel : {linha[4]}")

def updade_dispo():
    id = int(input("Digite o id do livro alterado ou removido: "))
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT disponivel FROM Biblioteca WHERE id = ?", (id,))
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
        """, (novo_status, id))

        conexao.commit()
        print(f"Status atualizado para '{novo_status}'.")
    else:
        print("Livro com o ID informado não encontrado.")

    conexao.close()


def remover():
    id = int(input("Digite o id do livro alterado ou removido: "))
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Biblioteca WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

def menu():
    while True:
        print("\n-----Menu-----")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar disponibilidade")
        print("4. Remover livro")
        print("5. Sair")
        escolha = int(input("Escolha o numero da opção desejada: "))
        if escolha == 1:
            cadastrar_livro()
            print("Livro cadastrado")
        elif escolha == 2:
            listar_livro()
        elif escolha == 3:
            updade_dispo()
        elif escolha == 4:
            remover()
        elif escolha == 5:
            print("Finalizando sistema!")
            break
        else:
            print("Escolha não identificada")
        
