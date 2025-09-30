import sqlite3
def cadastrar_livro():
    try:
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
        print("Livro cadastrado com sucesso!")
    except ValueError:
        print("Erro: o ano deve ser um número inteiro.")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
    finally:
        conexao.close()
def listar_livros():
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Biblioteca")
        livros = cursor.fetchall()
        if livros:
            for linha in livros:
                print(f"ID: {linha[0]} | Título: {linha[1]} | Ano: {linha[3]} | Autor: {linha[2]} | Disponível: {linha[4]}")
        else:
            print("Nenhum livro cadastrado.")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
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



def remover_livro():
    try:
        id = int(input("Digite o id do livro alterado ou removido: "))
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Biblioteca WHERE id = ?", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Livro removido com sucesso.")
        else:
            print("Livro com o ID informado não encontrado.")
    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
    finally:
        conexao.close()

def menu():
    while True:
        print("\n-----Menu-----")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar disponibilidade")
        print("4. Remover livro")
        print("5. Sair")
        try:
            escolha = int(input("Escolha o numero da opção desejada: "))
            if escolha == 1:
                cadastrar_livro()
            elif escolha == 2:
                listar_livros()
            elif escolha == 3:
                atualizar_disponibilidade()
            elif escolha == 4:
                remover_livro()
            elif escolha == 5:
                print("Finalizando sistema!")
                break
            else:
                print("Escolha não identificada")
        except ValueError:
            print("Erro: digite um número inteiro para a opção.")
        
