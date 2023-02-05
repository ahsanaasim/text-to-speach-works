import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

    def configure(self):
        self.setRate(30)

    def setRate(self, rate):
        self.engine.setProperty('rate', rate)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()