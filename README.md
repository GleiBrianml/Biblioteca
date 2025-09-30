# 📚 Sistema de Gerenciamento de Biblioteca

Este é um simples sistema de gerenciamento de biblioteca desenvolvido em **Python**, utilizando **Streamlit** para a interface web e **SQLite** como banco de dados. Ele permite:

- Cadastrar novos livros
- Listar livros existentes
- Atualizar a disponibilidade de livros
- Remover livros do acervo

---

## 🚀 Funcionalidades

### ✅ Cadastrar Livro
Adicione um novo livro ao banco de dados, preenchendo título, autor e ano de publicação.

### 📋 Listar Livros
Exibe todos os livros cadastrados, mostrando:
- ID
- Título
- Autor
- Ano
- Disponibilidade

### 🔄 Atualizar Disponibilidade
Altere o status de disponibilidade de um livro entre `Sim` e `Não`.

### 🗑️ Remover Livro
Exclua um livro do banco de dados permanentemente, com base em seu ID.

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Streamlit](https://streamlit.io/)

---

## 📁 Estrutura de Arquivos



---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/biblioteca-app.git
cd biblioteca-app

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install streamlit

CREATE TABLE IF NOT EXISTS Biblioteca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
);

