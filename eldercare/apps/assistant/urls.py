from django.urls import path
from .views_voice import voice_assistant, tts_demo

urlpatterns = [
    path("voice/", voice_assistant, name="voice_assistant"),
    path("tts-demo/", tts_demo, name="tts_demo"),
]
