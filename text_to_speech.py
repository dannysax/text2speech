import os
from gtts import gTTS


language = "en"

def convert_text_to_speech(text):
    gtts_object = gTTS(text=text, lang=language, slow=False)
    gtts_object.save("audio.mp3")
    os.system("audio.mp3")

convert_text_to_speech("Let's go to Mars!")