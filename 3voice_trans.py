from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout
import sys
from deep_translator import DeeplTranslator
import speech_recognition as sr
# from deeptrans import DeepTranslator
import time

# Recognize speech from the microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for English audio...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing audio...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I did not understand. Please repeat."
    except sr.RequestError:
        return "Sorry, the service is down."

# Translate the recognized text from English to Hindi using DeepTrans
def translate_to_hindi(text):
    translator = DeeplTranslator(source='en', target='hi')
    translated = translator.translate(text)
    return translated

# # Time check to ensure feature works only between 9:30 PM and 10:00 PM
def is_within_timeframe():
    current_time = time.localtime()
    return current_time.tm_hour == 18 and current_time.tm_min >= 30 and current_time.tm_min <= 59

# PyQt5 GUI setup
class VoiceTranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Translator")
        self.initUI()

    def initUI(self):
        self.text_display = QTextEdit(self)
        self.text_display.setPlaceholderText("Translated text will appear here...")
        
        self.listen_button = QPushButton("Start Listening", self)
        self.listen_button.clicked.connect(self.start_translating)
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.listen_button)
        self.layout.addWidget(self.text_display)
        
        self.setGeometry(300,300, 400, 300)

    def start_translating(self):
        if is_within_timeframe():
            recognized_text = recognize_speech()
            if recognized_text.lower() == "sorry, i did not understand. please repeat.":
                self.text_display.setText(recognized_text)
            else:
                translated_text = translate_to_hindi(recognized_text)
                self.text_display.setText(f"English: {recognized_text}\n\nHindi: {translated_text}")
        else:
            self.text_display.setText("Taking rest, see you tomorrow!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VoiceTranslatorApp()
    ex.show()
    sys.exit(app.exec_())
