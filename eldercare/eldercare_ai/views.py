from django.shortcuts import render
from django.http import JsonResponse

def realtime_assistant(request):
    if request.method == "GET":
        return render(request, "realtime.html")  # frontend page
    elif request.method == "POST":
        # Here you’d hook in Whisper + Ollama + Coqui pipeline
        return JsonResponse({"status": "ok", "msg": "Realtime pipeline coming soon"})
