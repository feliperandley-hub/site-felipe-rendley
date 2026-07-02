import streamlit as st

# Configuração da página - Adicionando ícone e nome na aba
st.set_page_config(page_title="Felipe Rendley | Fotografia", page_icon="📸", layout="wide")

# Estilização (CSS injetado para dar um ar mais premium)
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #000; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Layout com colunas para organizar melhor
col1, col2 = st.columns([1, 1])

with col1:
    st.title("📸 Felipe Rendley")
    st.subheader("Fotografia Profissional de Imóveis")
    st.write("Valorizando cada detalhe do seu espaço com um olhar apurado.")
    st.info("💡 Especialista em destacar os melhores ângulos de apartamentos e casas.")

with col2:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=600&auto=format&fit=crop", caption="Exemplo de qualidade")

st.markdown("---")

# Seção de Serviços em Destaque
st.header("Serviços")
c1, c2, c3 = st.columns(3)
c1.metric("Fotos HDR", "Qualidade")
c2.metric("Edição Premium", "Detalhe")
c3.metric("Entrega Rápida", "Agilidade")

st.markdown("---")

# Seção de Ação
st.header("🚀 Pronto para destacar seu imóvel?")
st.link_button("Ver Portfólio no Instagram", "https://www.instagram.com/felipe_rendley/")

# Formulário com melhor aparência
with st.expander("Clique aqui para solicitar um orçamento"):
    with st.form("form_contato_novo"):
        nome = st.text_input("Nome completo")
        whatsapp = st.text_input("WhatsApp para contato")
        imovel = st.text_area("Endereço ou link do imóvel")
        enviar = st.form_submit_button("Enviar mensagem")
        if enviar:
            st.success("Recebido! Entrarei em contato em breve.")
