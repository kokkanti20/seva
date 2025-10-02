from django.http import JsonResponse
from .speak_text import transcribe_audio, translate_text, chat_with_ollama, speak_text

def voice_assistant(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]
        file_path = f"/tmp/{audio_file.name}"

        # Save uploaded audio
        with open(file_path, "wb+") as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        # Step 1: Transcribe
        text = transcribe_audio(file_path)

        # Step 2: Translate to English (for LLM input)
        english_text = translate_text(text, "en")

        # Step 3: Generate Response
        response = chat_with_ollama(english_text)

        # Step 4: Translate back to original language
        final_text = translate_text(response, "te")  # Telugu example

        # Step 5: Convert to speech
        out_audio = speak_text(final_text)

        return JsonResponse({
            "input_text": text,
            "assistant_reply": final_text,
            "audio_file": out_audio
        })

    return JsonResponse({"error": "No audio uploaded"}, status=400)


# 👇 This is the missing function
def tts_demo(request):
    """
    Simple demo to prove Step 4 and 5 work:
    - Calls Ollama with a prompt
    - Speaks the response
    - Returns the audio URL
    """
    if request.method != "GET":
        return JsonResponse({"error": "Use GET"}, status=405)

    # STEP 4: Ask your local LLM something
    reply_text = chat_with_ollama("Say hello and introduce yourself briefly.")

    # STEP 5: Speak the reply (choose lang, e.g., 'en', 'te', 'hi')
    out_audio = speak_text(reply_text, lang="en")

    return JsonResponse({
        "llm_reply": reply_text,
        "audio_file": out_audio
    })
