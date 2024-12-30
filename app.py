import os
import streamlit as st
import requests
import tempfile

# Configurações da API
groq_api_key = "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"
groq_api_endpoint = "https://api.groq.com/openai/v1/audio/transcriptions"
headers = {"Authorization": f"Bearer {groq_api_key}"}

# Função para transcrever áudio
def transcribe_audio(file_path, model="whisper-large-v3-turbo", language="pt"):
    file_extension = os.path.splitext(file_path)[1].lower()

    # Determina o tipo MIME baseado na extensão
    if file_extension == '.mp3':
        mime_type = 'audio/mp3'
    elif file_extension == '.wav':
        mime_type = 'audio/wav'
    else:
        st.error(f"Formato de arquivo não suportado: {file_extension}")
        return ""

    with open(file_path, "rb") as audio_file:
        files = {"file": (file_path, audio_file, mime_type)}
        data = {
            "model": model,
            "language": language,
            "response_format": "json",
        }
        response = requests.post(groq_api_endpoint, headers=headers, files=files, data=data)
        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            st.error(f"Erro na API: {response.status_code} - {response.text}")
            return ""

# Interface do Streamlit
st.title("Transcrição de Áudio com API Groq")

# Upload de arquivo de áudio
uploaded_file = st.file_uploader("Envie seu arquivo de áudio", type=["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        temp_audio_file.write(uploaded_file.read())
        temp_audio_path = temp_audio_file.name
    st.audio(uploaded_file, format="audio/mp3")
    if st.button("Transcrever áudio"):
        try:
            transcription = transcribe_audio(temp_audio_path)
            st.subheader("Transcrição:")
            st.text_area("Texto transcrito", transcription, height=200)
            
            # Botão para baixar a transcrição
            st.download_button(
                label="Baixar Transcrição",
                data=transcription,
                file_name="transcricao.txt",
                mime="text/plain"
            )
        finally:
            if os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)
