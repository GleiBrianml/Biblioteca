import streamlit as st
from funcoes_app import (
    cadastrar_livro,
    listar_livros,
    atualizar_disponibilidade,
    remover_livro
)

st.set_page_config(page_title="Biblioteca", layout="centered")
st.title("📚 Sistema de Biblioteca")

menu = st.sidebar.radio("Menu", ["Cadastrar Livro", "Listar Livros", "Atualizar Disponibilidade", "Remover Livro"])

if menu == "Cadastrar Livro":
    st.subheader("Cadastrar novo livro")
    with st.form("form_livro"):
        titulo = st.text_input("Título")
        autor = st.text_input("Autor")
        ano = st.number_input("Ano", min_value=0, max_value=9999, step=1)
        enviar = st.form_submit_button("Cadastrar")
        if enviar:
            if titulo and autor:
                sucesso, msg = cadastrar_livro(titulo, autor, int(ano))
                st.success(msg) if sucesso else st.error(msg)
            else:
                st.warning("Preencha todos os campos.")

elif menu == "Listar Livros":
    st.subheader("📋 Lista de Livros")
    livros = listar_livros()
    if livros:
        st.dataframe(
            [{"ID": l[0], "Título": l[1], "Autor": l[2], "Ano": l[3], "Disponível": l[4]} for l in livros]
        )
    else:
        st.info("Nenhum livro cadastrado.")

elif menu == "Atualizar Disponibilidade":
    st.subheader("🔄 Atualizar disponibilidade")
    livros = listar_livros()
    if livros:
        opcoes = {f"{l[0]} - {l[1]} ({l[4]})": l[0] for l in livros}
        escolha = st.selectbox("Selecione o livro", list(opcoes.keys()))
        if st.button("Atualizar"):
            sucesso, msg = atualizar_disponibilidade(opcoes[escolha])
            st.success(msg) if sucesso else st.error(msg)
            st.experimental_rerun()
    else:
        st.info("Nenhum livro para atualizar.")

elif menu == "Remover Livro":
    st.subheader("🗑️ Remover Livro")
    livros = listar_livros()
    if livros:
        opcoes = {f"{l[0]} - {l[1]}": l[0] for l in livros}
        escolha = st.selectbox("Selecione o livro", list(opcoes.keys()))
        if st.button("Remover"):
            sucesso, msg = remover_livro(opcoes[escolha])
            st.success(msg) if sucesso else st.error(msg)
            st.experimental_rerun()
    else:
        st.info("Nenhum livro para remover.")

