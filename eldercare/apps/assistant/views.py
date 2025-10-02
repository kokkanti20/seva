from django.shortcuts import render
from django.http import JsonResponse

def realtime_assistant(request):
    if request.method == "GET":
        # Render a frontend page for realtime chat
        return render(request, "realtime.html")

    elif request.method == "POST":
        # Later hook Whisper + Ollama + Coqui here
        return JsonResponse({"status": "ok", "message": "Realtime pipeline not implemented yet"})
