from .stt import speech_to_text
from .llm import ask_ollama
from .tts import text_to_speech

def voice_assistant(audio_file: str) -> str:
    """
    Complete pipeline:
    Audio → Whisper → Ollama → Coqui TTS
    """
    # 1. Convert speech to text
    user_text = speech_to_text(audio_file)

    # 2. Generate response using Ollama
    response = ask_ollama(f"You are a helpful eldercare assistant. User said: {user_text}")

    # 3. Convert response back to audio
    audio_path = text_to_speech(response, "static/response.wav")

    return {"user_text": user_text, "response_text": response, "audio_file": audio_path}
