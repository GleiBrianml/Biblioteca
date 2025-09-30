# funcoes.py

import sqlite3

def cadastrar_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO Biblioteca (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, "Sim"))
        conexao.commit()
        return True, "Livro cadastrado com sucesso!"
    except sqlite3.Error as e:
        return False, f"Erro no banco de dados: {e}"
    finally:
        conexao.close()


def listar_livros():
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Biblioteca")
        livros = cursor.fetchall()
        return livros
    except sqlite3.Error as e:
        return []
    finally:
        conexao.close()


def atualizar_disponibilidade(id):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT disponivel FROM Biblioteca WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado:
            status_atual = resultado[0]
            novo_status = "Não" if status_atual.lower() == "sim" else "Sim"
            cursor.execute("""
                UPDATE Biblioteca
                SET disponivel = ?
                WHERE id = ?
            """, (novo_status, id))
            conexao.commit()
            return True, f"Status atualizado para '{novo_status}'."
        else:
            return False, "Livro com o ID informado não encontrado."
    except sqlite3.Error as e:
        return False, f"Erro no banco de dados: {e}"
    finally:
        conexao.close()


def remover_livro(id):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Biblioteca WHERE id = ?", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            return True, "Livro removido com sucesso."
        else:
            return False, "Livro com o ID informado não encontrado."
    except sqlite3.Error as e:
        return False, f"Erro no banco de dados: {e}"
    finally:
        conexao.close()
