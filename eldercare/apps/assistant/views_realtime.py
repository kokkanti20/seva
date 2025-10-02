# apps/assistant/views_realtime.py
import os
import requests
from django.http import JsonResponse

def create_realtime_session(request):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return JsonResponse({"error": "Missing OpenAI API key"}, status=500)

        response = requests.post(
            "https://api.openai.com/v1/realtime/sessions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "gpt-4o-realtime-preview-2024-12-17",
                "voice": "verse"
            }
        )

        if response.status_code != 200:
            return JsonResponse({"error": response.text}, status=response.status_code)

        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
