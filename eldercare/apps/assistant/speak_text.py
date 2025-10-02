from gtts import gTTS
from pydub import AudioSegment
import os
import subprocess
import whisper

# Load Whisper model once
model = whisper.load_model("small")


# 🎤 Step 1: Transcribe Audio
def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(file_path)
    return result["text"]


# 🌍 Step 2: Translate text (dummy – just returns same text for now)
def translate_text(text: str, target_lang: str = "en") -> str:
    """
    You can later replace this with HuggingFace transformers or Google Translate API.
    For now, just return the original text so pipeline doesn't break.
    """
    return text


# 🤖 Step 3: Chat with Ollama (local LLM)
def chat_with_ollama(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            capture_output=True,
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[Error calling Ollama: {e}]"


# 🔊 Step 4 & 5: Convert text to speech
def speak_text(text: str, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = f"media/output_{lang}.mp3"
    tts.save(filename)
    return filename
