from googletrans import Translator
def translate_to_hindi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text

# Example usage
text = "Hello, how are you?"
translated_text = translate_to_hindi(text)
print(translated_text)  # Output will be the Hindi translation
