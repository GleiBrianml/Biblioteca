# 📚 Sistema de Gerenciamento de Biblioteca com SQLite

Este é um simples sistema de gerenciamento de livros feito em **Python**, com uso de **SQLite** para persistência de dados. Ele permite cadastrar, listar, atualizar disponibilidade e remover livros de uma biblioteca local.

## 🛠 Requisitos

- Python 3.x
- Biblioteca padrão `sqlite3` (já vem com o Python)

## 🗄 Estrutura da Tabela

O banco de dados `Biblioteca.db` contém uma tabela chamada `Biblioteca` com os seguintes campos:

| Campo       | Tipo     | Descrição                       |
|-------------|----------|----------------------------------|
| `id`        | INTEGER  | Chave primária (autoincremento) |
| `titulo`    | TEXT     | Título do livro                 |
| `autor`     | TEXT     | Nome do autor                   |
| `ano`       | INTEGER  | Ano de publicação               |
| `disponivel`| TEXT     | Status de disponibilidade       |

**Criação da Tabela (caso ainda não exista):**
```python
import sqlite3

conexao = sqlite3.connect("Biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Biblioteca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()
