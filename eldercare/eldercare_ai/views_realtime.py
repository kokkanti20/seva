import os
import tempfile
import subprocess
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
import whisper
from TTS.api import TTS  # Coqui TTS

# Load once
whisper_model = whisper.load_model("small")
tts_model = TTS(model_name=settings.TTS_MODEL, progress_bar=False, gpu=False)

def realtime_assistant(request):
    """Render the frontend page with mic controls."""
    return render(request, "assistant/realtime.html")


def realtime_api(request):
    """
    Full free pipeline:
    1. Save uploaded audio
    2. Transcribe (Whisper)
    3. Chat with Ollama
    4. Generate speech with Coqui
    """
    if request.method != "POST" or "audio" not in request.FILES:
        return HttpResponseBadRequest("Upload audio via POST")

    audio_file = request.FILES["audio"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        for chunk in audio_file.chunks():
            tmp.write(chunk)
        tmp_path = tmp.name

    # Step 1: STT
    result = whisper_model.transcribe(tmp_path)
    user_text = result["text"]

    # Step 2: Chat with Ollama (local model must be running: ollama serve)
    prompt = f"User said: {user_text}. Reply naturally."
    try:
        ollama_output = subprocess.check_output(
            ["ollama", "run", settings.OLLAMA_MODEL, prompt],
            universal_newlines=True
        )
    except Exception as e:
        ollama_output = f"(Ollama error: {e})"
    reply_text = ollama_output.strip()

    # Step 3: TTS (Coqui → audio)
    output_path = os.path.join(settings.MEDIA_ROOT, "realtime_reply.wav")
    tts_model.tts_to_file(text=reply_text, file_path=output_path)

    audio_url = settings.MEDIA_URL + "realtime_reply.wav"

    return JsonResponse({
        "transcribed": user_text,
        "assistant_reply": reply_text,
        "audio_url": audio_url,
    })
