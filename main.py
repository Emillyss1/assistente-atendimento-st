import streamlit as st

# Configuração da página (Estilo Clean/Einstein)
st.set_page_config(page_title="Treinamento PNH - Einstein", page_icon="🏥")

# CSS para deixar os botões maiores e com a cara do Einstein
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .stAudio { margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Inicialização do estado da sessão (para o quiz não resetar ao clicar)
if 'pergunta_idx' not in st.session_state:
    st.session_state.pergunta_idx = 0
    st.session_state.acertos = 0

perguntas = [
    {
        "situacao": "Um paciente reclama da demora no atendimento de forma ríspida na recepção.",
        "opcoes": ["A) Informar que deve aguardar", "B) Chamar a segurança", "C) Validar a frustração e oferecer previsão", "D) Ignorar"],
        "correta": "C",
        "audio": "pergunta1.mp3"
    },
    # Adicione as outras aqui seguindo o mesmo padrão...
]

st.title("🏥 Simulador de Atendimento SPA")
st.subheader("Protagonismo e Humanização no Einstein")

if st.session_state.pergunta_idx < len(perguntas):
    p = perguntas[st.session_state.pergunta_idx]
    
    st.info(f"**Situação {st.session_state.pergunta_idx + 1}:** {p['situacao']}")
    
    # Player de Áudio
    with open(p['audio'], 'rb') as f:
        st.audio(f.read(), format="audio/mp3")

    # Botões de Resposta
    for idx, opcao in enumerate(p['opcoes']):
        if st.button(opcao):
            letra = chr(65 + idx) # Converte 0 para A, 1 para B...
            if letra == p['correta']:
                st.session_state.acertos += 1
            
            st.session_state.pergunta_idx += 1
            st.rerun()

else:
    # Resultado Final
    porcentagem = (st.session_state.acertos / len(perguntas)) * 100
    st.success(f"### 🎉 Treinamento Concluído!")
    st.metric("Sua Pontuação de Humanização", f"{porcentagem}%")
    
    if st.button("Reiniciar Simulador"):
        st.session_state.pergunta_idx = 0
        st.session_state.acertos = 0
        st.rerun()