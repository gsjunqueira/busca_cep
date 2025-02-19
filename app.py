""" Sistema de Busca de CEP """

import streamlit as st
import requests

def busca_cep(c_e_p):
    """ Função para buscar o CEP"""
    try:
        return requests.get(f"https://viacep.com.br/ws/{c_e_p}/json/", timeout=10)
    except ImportError:
        return False


st.set_page_config(page_title="Busca CEP", page_icon='📭')
st.title('Sistema de busca de CEP')
st.divider()

menu = st.sidebar
cep = menu.text_input("Digite o CEP:")
botao = menu.button("pesquisar")

if botao:
    resposta = busca_cep(cep)
    if resposta.status_code == 200:
        st.success("CEP encontrado com sucesso!", icon='✅')
        dados = resposta.json()

        col1, col2 = st.columns(2)

        col1.markdown(f"**CEP:** {dados['cep']}")
        col1.markdown(f"**Logradouro:** {dados['logradouro']}")
        col1.markdown(f"**Complemento:** {dados['complemento']}")
        col1.markdown(f"**Unidade:** {dados['unidade']}")
        col1.markdown(f"**Bairro:** {dados['bairro']}")
        col1.markdown(f"**Localidade:** {dados['localidade']}")
        col2.markdown(f"**UF:** {dados['uf']}")
        col2.markdown(f"**Código IBGE:** {dados['ibge']}")
        col2.markdown(f"**GIA:** {dados['gia']}")
        col2.markdown(f"**DDD:** {dados['ddd']}")
        col2.markdown(f"**SIAFI:** {dados['siafi']}")
    else:
        st.error("o CEP informado é inválido!", icon='❌')
