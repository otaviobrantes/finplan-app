import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Resumo Orçado x Real",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Resumo Orçado x Real")

if 'cliente_data' not in st.session_state:
    st.session_state.cliente_data = {}

with st.container():
    st.header("👤 Dados do Cliente")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Informações Pessoais")
        nome = st.text_input("Nome completo", value=st.session_state.cliente_data.get('nome', ''))
        data_nascimento = st.date_input("Data de Nascimento", value=st.session_state.cliente_data.get('data_nascimento', datetime(1980, 1, 1)))
        nacionalidade = st.text_input("Nacionalidade", value=st.session_state.cliente_data.get('nacionalidade', 'Brasileira'))
        estado_civil = st.selectbox("Estado Civil", ["Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)", "União Estável"], index=0)
        regime_bens = st.text_input("Regime de bens", value=st.session_state.cliente_data.get('regime_bens', 'Comunhão Parcial de Bens'))
    
    with col2:
        st.subheader("Endereço e Contato")
        endereco_residencial = st.text_input("Endereço Residencial", value=st.session_state.cliente_data.get('endereco_residencial', ''))
        bairro_cidade = st.text_input("Bairro / Cidade", value=st.session_state.cliente_data.get('bairro_cidade', ''))
        cep = st.text_input("CEP", value=st.session_state.cliente_data.get('cep', ''))
        email_principal = st.text_input("E-mail principal", value=st.session_state.cliente_data.get('email_principal', ''))

st.header("🎓 Dados Profissionais e Receitas")

with st.expander("Dados Profissionais", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        profissao = st.text_input("Profissão", value=st.session_state.cliente_data.get('profissao', ''))
        empresa1 = st.text_input("Empresa 1", value=st.session_state.cliente_data.get('empresa1', ''))
        cnpj = st.text_input("CNPJ", value=st.session_state.cliente_data.get('cnpj', ''))
        cargo = st.text_input("Cargo", value=st.session_state.cliente_data.get('cargo', ''))
    
    with col2:
        fonte_remuneracao1 = st.number_input("Fonte Remuneração 1 (R$)", value=0.0, step=1000.0, format="%.2f")
        inss = st.number_input("INSS (R$)", value=0.0, step=100.0, format="%.2f")
        total_remuneracao_bruta = st.number_input("Total Remuneração BRUTA (R$)", value=0.0, step=1000.0, format="%.2f")

if st.button("💾 Salvar Dados"):
    st.session_state.cliente_data = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'nacionalidade': nacionalidade,
        'estado_civil': estado_civil,
        'regime_bens': regime_bens,
        'endereco_residencial': endereco_residencial,
        'bairro_cidade': bairro_cidade,
        'cep': cep,
        'email_principal': email_principal,
        'profissao': profissao,
        'empresa1': empresa1,
        'cnpj': cnpj,
        'cargo': cargo
    }
    st.success("Dados salvos com sucesso!")

st.caption("FinPlan - Sistema em desenvolvimento")
