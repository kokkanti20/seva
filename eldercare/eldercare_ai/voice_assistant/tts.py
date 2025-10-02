from TTS.api import TTS

# Use a free multilingual model
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def text_to_speech(text: str, output_file: str = "response.wav"):
    """Convert text to speech"""
    tts.tts_to_file(text=text, file_path=output_file)
    return output_file
