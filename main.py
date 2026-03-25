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
            "opcoes": [
                "A) Informar que o sistema está lento e que ele deve aguardar sentado.",
                "B) Chamar a segurança, pois ele está alterando o clima organizacional.",
                "C) Validar a frustração dele, explicar o fluxo e oferecer uma previsão real.",
                "D) Ignorar as reclamações para não gerar mais conflito."
            ],
            "correta": "C",
            "audio": "audio/situacao1.mp3"
        },
        {
            "situacao": "Um colega de trabalho está sobrecarregado e cometendo erros de digitação.",
            "opcoes": [
                "A) Reportar os erros imediatamente à supervisão para evitar falhas.",
                "B) Praticar a Sinergia de Equipe, oferecendo apoio para reorganizar as tarefas.",
                "C) Fazer o trabalho dele em silêncio para não causar constrangimento.",
                "D) Dizer que ele precisa de um curso de reciclagem urgente."
            ],
            "correta": "B",
            "audio": "audio/situacao2.mp3"
        },
        {
            "situacao": "A família de um paciente quer saber informações que você não tem autorização para dar.",
            "opcoes": [
                "A) Dizer apenas: 'Não sou autorizado a falar, pergunte ao médico'.",
                "B) Inventar uma informação genérica para acalmar a família.",
                "C) Praticar o Acolhimento: ouvir a dúvida e encaminhá-los ao profissional responsável.",
                "D) Pedir para que a família se retire do setor imediatamente."
            ],
            "correta": "C",
            "audio": "audio/situacao3.mp3"
        },
        {
            "situacao": "Em uma reunião de equipe, surge uma ideia para melhorar a jornada do paciente.",
            "opcoes": [
                "A) Rejeitar, pois as normas da instituição já são consolidadas.",
                "B) Deixar que apenas os médicos decidam, pois são as autoridades.",
                "C) Valorizar o Protagonismo e a Transversalidade, debatendo a ideia com todos.",
                "D) Aceitar apenas se a ideia não gerar mais trabalho para a equipe."
            ],
            "correta": "C",
            "audio": "audio/situacao4.mp3"
        }
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