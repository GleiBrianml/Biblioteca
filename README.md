# 📚 Sistema de Biblioteca com Streamlit e SQLite

Este é um sistema simples de gerenciamento de livros, desenvolvido com **Python**, utilizando **Streamlit** para a interface gráfica e **SQLite** como banco de dados. O sistema permite:

- Cadastrar novos livros
- Listar todos os livros cadastrados
- Atualizar a disponibilidade dos livros
- Remover livros do acervo

## 🚀 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SQLite3](https://www.sqlite.org/index.html)

---

## 📂 Estrutura do Projeto

- 📁 seu_projeto/
- │
- ├── 📄 app.py # Interface principal com Streamlit
- ├── 📄 funcoes_app.py # Arquivo com as funções de manipulação do banco
- └── 📄 Biblioteca.db # Banco de dados SQLite (gerado automaticamente)

---

## ⚙️ Funcionalidades

### ✅ Cadastrar Livro
Adiciona um novo livro à base de dados, com título, autor e ano. O campo "Disponível" é definido como "Sim" por padrão.

### 📋 Listar Livros
Exibe todos os livros cadastrados no sistema em uma tabela com as seguintes colunas:
- ID
- Título
- Autor
- Ano
- Disponível

### 🔄 Atualizar Disponibilidade
Alterna o status de disponibilidade de um livro entre "Sim" e "Não".

### 🗑️ Remover Livro
Remove um livro da base de dados com base no ID selecionado.

---

## 🛠️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

pip install streamlit

streamlit run app.py

CREATE TABLE IF NOT EXISTS Biblioteca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel TEXT NOT NULL
);
