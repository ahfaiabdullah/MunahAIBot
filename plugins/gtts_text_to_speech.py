from gtts import gTTS
import os
import uuid

def teks_ke_suara(text: str) -> str:
    tts = gTTS(text=text, lang='ms')
    filename = f"/tmp/munah_audio_{uuid.uuid4()}.mp3"
    tts.save(filename)
    return filename