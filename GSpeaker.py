from gtts import gTTS
import os

class GSpeaker:
    def __init__(self, text=""):
        self.engine = gTTS(text=text, lang="en", 
                           slow=True, tld="co.in")

    def speak(self):
        self.engine.save("audios/audio.mp3")
        # os.system("start example.mp3")