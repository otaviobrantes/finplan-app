import streamlit as st

st.set_page_config(
    page_title="Orçamento Mensal",
    layout="wide",
    page_icon="💰"
)

st.title("💰 Orçamento Familiar")

if 'orcamento_data' not in st.session_state:
    st.session_state.orcamento_data = {}

st.header("📥 ENTRADAS")

with st.expander("Entradas Mensais", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Descrição")
        st.write("Salário Líquido")
        st.write("Outras entradas")
        st.write("**Total ENTRADAS**")
    
    with col2:
        st.subheader("Valor mensal")
        salario_liquido = st.number_input("salario_mensal", value=0.0, step=1000.0, format="%.2f", label_visibility="collapsed")
        outras_entradas = st.number_input("outras_entradas", value=0.0, step=1000.0, format="%.2f", label_visibility="collapsed")
        total_entradas = salario_liquido + outras_entradas
        st.write(f"**R$ {total_entradas:,.2f}**")

st.header("📤 SAÍDAS")

with st.expander("Despesas Essenciais", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Aluguel/Prestação")
        st.write("Condomínio")
        st.write("Supermercado")
        st.write("Transporte")
        st.write("**Total Essenciais**")
    
    with col2:
        aluguel = st.number_input("aluguel", value=0.0, step=500.0, format="%.2f", label_visibility="collapsed")
        condominio = st.number_input("condominio", value=0.0, step=500.0, format="%.2f", label_visibility="collapsed")
        supermercado = st.number_input("supermercado", value=0.0, step=500.0, format="%.2f", label_visibility="collapsed")
        transporte = st.number_input("transporte", value=0.0, step=500.0, format="%.2f", label_visibility="collapsed")
        total_essenciais = aluguel + condominio + supermercado + transporte
        st.write(f"**R$ {total_essenciais:,.2f}**")

# Resultado
st.header("📊 RESULTADO")

resultado = total_entradas - total_essenciais

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Entradas", f"R$ {total_entradas:,.2f}")
with col2:
    st.metric("Total Saídas", f"R$ {total_essenciais:,.2f}")

if resultado >= 0:
    st.success(f"✅ Superávit: R$ {resultado:,.2f}")
else:
    st.error(f"❌ Déficit: R$ {abs(resultado):,.2f}")

if st.button("💾 Salvar Orçamento"):
    st.session_state.orcamento_data = {
        'salario_liquido': salario_liquido,
        'outras_entradas': outras_entradas,
        'aluguel': aluguel,
        'condominio': condominio,
        'supermercado': supermercado,
        'transporte': transporte
    }
    st.success("Orçamento salvo com sucesso!")

st.caption("FinPlan - Sistema em desenvolvimento")
