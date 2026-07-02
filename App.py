import streamlit as st

st.set_page_config(page_title="Felipe Rendley | Fotografia", layout="centered")

st.title("📸 Felipe Rendley")
st.subheader("Fotografia Profissional de Imóveis")

# Botão direto para o seu Insta
st.link_button("Ver meu Portfólio no Instagram", "https://www.instagram.com/felipe_rendley/")

st.markdown("---")

st.header("📩 Solicite um Orçamento")
with st.form("form_contato", clear_on_submit=True):
    nome = st.text_input("Seu Nome")
    telefone = st.text_input("Seu Telefone/WhatsApp")
    msg = st.text_area("Descreva o imóvel")
    enviar = st.form_submit_button("Enviar")
    if enviar:
        st.success("Mensagem recebida! Entrarei em contato.")
