import streamlit as st

# Inicializa o estado da tela se não existir
if 'tela_ativa' not in st.session_state:
    st.session_state.tela_ativa = "inicio"

# --- TELA DE INTRODUÇÃO ---
if st.session_state.tela_ativa == "inicio":
    st.title("🏥 Simulador SPA: Humanização na Prática")

    with open("apresentacao.mp3", 'rb') as f:
            st.audio(f.read(), format="audio/mp3")

    st.markdown("""
    ### Bem-vinda(o) ao Treinamento de Atendimento
    Este simulador foi desenvolvido como parte da capacitação do **Hospital Albert Einstein**. 
    O objetivo é aplicar os conceitos de:
    * **S** - Segurança
    * **P** - Paixão em servir
    * **A** - Atenção aos detalhes
    
    **Instruções:**
    1. Você ouvirá uma situação real de atendimento.
    2. Escolha a opção que melhor reflete um atendimento humanizado.
    3. Ao final, você receberá seu índice de aproveitamento.
    """)
    
    if st.button("🚀 Começar Simulação"):
        st.session_state.tela_ativa = "quiz"
        st.rerun()

    st.divider()
    st.caption("Desenvolvido por: Emilly Rayanna | Desenvolvedora python")

# --- TELA DO QUIZ (código anterior) ---
elif st.session_state.tela_ativa == "quiz":
    st.title("📝 Quiz de Situações")
    
    # Configuração da página (Estilo Clean/Einstein)
    st.set_page_config(page_title="Treinamento PNH - Einstein", page_icon="🏥")

    # CSS para deixar os botões maiores e com a cara do Einstein
    st.markdown("""
        <style>
        .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; color: black; background-color: white; }
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
                "audio": "Pergunta1.mp3"
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
                "audio": "Pergunta2.mp3"
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
                "audio": "Pergunta3.mp3"
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
                "audio": "Pergunta4.mp3"
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
        with open("concluido.mp3", 'rb') as f:
            st.audio(f.read(), format="audio/mp3")

        if porcentagem==0:
            with open("zero.mp3", 'rb') as f:
                st.audio(f.read(), format="audio/mp3")
        elif porcentagem == 25:
            with open("vintecinco.mp3", 'rb') as f:
                st.audio(f.read(), format="audio/mp3")
        elif porcentagem == 50:
            with open("cinquenta.mp3", 'rb') as f:
                st.audio(f.read(), format="audio/mp3")
        elif porcentagem == 75:
            with open("cetentaecinco.mp3", 'rb') as f:
                st.audio(f.read(), format="audio/mp3")
        elif porcentagem == 100:
            with open("cem.mp3", 'rb') as f:
                st.audio(f.read(), format="audio/mp3")
        st.metric("Sua Pontuação de Humanização", f"{porcentagem}%")
        
        if st.button("Reiniciar Simulador"):
            st.session_state.pergunta_idx = 0
            st.session_state.acertos = 0
            st.rerun()# [O resto do seu código de perguntas aqui...]
    
    # Exemplo de botão para voltar
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.tela_ativa = "inicio"
        st.session_state.pergunta_idx = 0 # Reseta o quiz
        st.rerun()