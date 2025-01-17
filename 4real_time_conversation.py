import speech_recognition as sr
import pyttsx3
import requests
# import pywintypes
# DeepL API Configuration
DEEPL_API_KEY = "your-deepl-api-key"  # Replace with your DeepL API Key
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')

# Functions
def speak(text, language):
    """
    Convert text to speech.
    """
    if language == 'es':
        engine.setProperty('voice', voices[0].id)  # Adjust based on system Spanish voice
    elif language == 'en':
        engine.setProperty('voice', voices[1].id)  # Adjust based on system English voice
    engine.say(text)
    engine.runAndWait()

def translate_text_deepl(text, src_lang, dest_lang):
    """
    Translate text using DeepL API.
    """
    params = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "source_lang": src_lang.upper(),
        "target_lang": dest_lang.upper(),
    }
    response = requests.post(DEEPL_API_URL, data=params)
    if response.status_code == 200:
        return response.json()["translations"][0]["text"]
    else:
        print("Translation error:", response.text)
        return "Translation failed."

def speech_to_text(language):
    """
    Convert speech to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening ({language})...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand. Please repeat."
    except sr.RequestError:
        return "Speech service is unavailable."

def real_time_conversation():
    """
    Real-time conversation between English and Spanish speakers.
    """
    print("Starting real-time conversation...")
    print("Press Ctrl+C to exit.")
    try:
        while True:
            # English speaker
            print("English speaker, please speak...")
            english_text = speech_to_text(language='en-US')
            if english_text:
                print(f"English (Input): {english_text}")
                translated_to_spanish = translate_text_deepl(english_text, 'EN', 'ES')
                print(f"Translated to Spanish: {translated_to_spanish}")
                speak(translated_to_spanish, 'es')

            # Spanish speaker
            print("Spanish speaker, please speak...")
            spanish_text = speech_to_text(language='es-ES')
            if spanish_text:
                print(f"Spanish (Input): {spanish_text}")
                translated_to_english = translate_text_deepl(spanish_text, 'ES', 'EN')
                print(f"Translated to English: {translated_to_english}")
                speak(translated_to_english, 'en')
    except KeyboardInterrupt:
        print("\nConversation ended.")
        return

# Run the program
if __name__ == "__main__":
    real_time_conversation()
