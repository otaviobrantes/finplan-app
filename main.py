import streamlit as st

st.set_page_config(
    page_title="FinPlan - Sistema Financeiro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💰 FinPlan - Sistema Financeiro")
st.markdown("---")

st.header("Bem-vindo ao FinPlan")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Status", "Online")
    
with col2:
    st.metric("Módulos", "2 Implementados")
    
with col3:
    st.metric("Próximos", "Em Desenvolvimento")

st.markdown("""
### 📋 Módulos Disponíveis:
1. **Resumo Orçado x Real** - Dados do cliente
2. **Orçamento mensal** - Controle financeiro

### 🎯 Como usar:
- Navegue pelas páginas na barra lateral
- Preencha os dados do cliente
- Os dados são salvos temporariamente

*Sistema em desenvolvimento - versão beta*
""")

# Inicializar session_states
if 'cliente_data' not in st.session_state:
    st.session_state.cliente_data = {}

if 'orcamento_data' not in st.session_state:
    st.session_state.orcamento_data = {}
