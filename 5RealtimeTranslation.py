# import PyQt5
# import cv2
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# from datetime import datetime

# # Sample dictionary for English to Hindi translation
# translation_dict = {
#     "cat": "\u092c\u093f\u0932\u094d\u0932\u0940",
#     "dog": "\u0915\u0941\u0924\u094d\u0924\u093e",
#     "tree": "\u092a\u0947\u0921\u093c",
#     "book": "\u0915\u093f\u0924\u093e\u092c"
# }

# class TranslationApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("English to Hindi Translator")
#         self.setGeometry(100, 100, 400, 200)

#         layout = QVBoxLayout()

#         self.label = QLabel("Enter an English word:")
#         layout.addWidget(self.label)

#         self.input_field = QLineEdit()
#         layout.addWidget(self.input_field)

#         self.translate_button = QPushButton("Translate")
#         self.translate_button.clicked.connect(self.translate_word)
#         layout.addWidget(self.translate_button)

#         self.output_label = QLabel("Translation:")
#         layout.addWidget(self.output_label)

#         self.setLayout(layout)

#     def translate_word(self):
#         word = self.input_field.text().strip().lower()

#         if not word:
#             QMessageBox.warning(self, "Input Error", "Please enter a word.")
#             return

#         current_time = datetime.now().time()
#         start_time = datetime.strptime("21:00:00", "%H:%M:%S").time()
#         end_time = datetime.strptime("22:00:00", "%H:%M:%S").time()

#         if word[0] in "aeiou":
#             if start_time <= current_time <= end_time:
#                 if word in translation_dict:
#                     self.output_label.setText(f"Translation: {translation_dict[word]}")
#                 else:
#                     QMessageBox.warning(self, "Translation Error", "Word not found in the dictionary.")
#             else:
#                 QMessageBox.warning(self, "Time Restriction", "This word starts with a vowel. Translations are allowed only between 9 PM and 10 PM.")
#         else:
#             if word in translation_dict:
#                 self.output_label.setText(f"Translation: {translation_dict[word]}")
#             else:
#                 QMessageBox.warning(self, "Translation Error", "Word not found in the dictionary.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     translator = TranslationApp()
#     translator.show()
#     sys.exit(app.exec_())

import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

# Sample dictionary for English to Hindi translation
translation_dict = {
    "cat": "\u092c\u093f\u0932\u094d\u0932\u0940",
    "dog": "\u0915\u0941\u0924\u094d\u0924\u093e",
    "tree": "\u092a\u0947\u0921\u093c",
    "book": "\u0915\u093f\u0924\u093e\u092c"
}

class TranslationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("English to Hindi Translator")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter an English word:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate_word)
        layout.addWidget(self.translate_button)

        self.output_label = QLabel("Translation:")
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def translate_word(self):
        word = self.input_field.text().strip().lower()

        if not word:
            QMessageBox.warning(self, "Input Error", "Please enter a word.")
            return

        current_time = datetime.now().time()
        start_time = datetime.strptime("21:00:00", "%H:%M:%S").time()
        end_time = datetime.strptime("22:00:00", "%H:%M:%S").time()

        if word[0] in "aeiou":
            if start_time <= current_time <= end_time:
                if word in translation_dict:
                    self.output_label.setText(f"Translation: {translation_dict[word]}")
                else:
                    QMessageBox.warning(self, "Translation Error", "Word not found in the dictionary.")
            else:
                QMessageBox.warning(self, "Time Restriction", "This word starts with a vowel. Translations are allowed only between 9 PM and 10 PM.")
        else:
            if word in translation_dict:
                self.output_label.setText(f"Translation: {translation_dict[word]}")
            else:
                QMessageBox.warning(self, "Translation Error", "Word not found in the dictionary.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = TranslationApp()
    translator.show()
    sys.exit(app.exec_())
