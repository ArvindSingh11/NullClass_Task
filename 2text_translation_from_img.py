import sys
import cv2
import pytesseract

from deep_translator import GoogleTranslator # first i used googlrtrans but due to unavaibility of cgi module in py 3.13 i shifted to deeptranslator
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel,QPushButton, QVBoxLayout,QFileDialog, QWidget, QTextEdit,QComboBox
)
from PyQt5.QtGui import QPixmap,QImage, QFont
from PyQt5.QtCore import Qt

# Configure Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path for your system

class TextTranslateApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Translator (using deep-translator)
        self.translator = GoogleTranslator()

        # Window properties
        self.setWindowTitle("Image & Video Text Translator")
        self.setGeometry(100, 100, 800,600)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Widgets starts from here
        self.label = QLabel("No Image/Video Loaded", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: #ffffff; border: 2px solid #dcdcdc; border-radius: 10px;")

        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("background-color: #ffffff; border: 1px solid #dcdcdc; padding: 10px;")

        self.language_selector = QComboBox(self)
        self.language_selector.addItems(["fr (French)", "es (Spanish)", "de (German)", "hi (Hindi)"])
        self.language_selector.setCurrentIndex(0)
        self.language_selector.setStyleSheet("background-color: #ffffff; border: 1px solid #dcdcdc;")

        self.load_image_button = QPushButton("Load Image", self)
        self.load_image_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius:5px; padding: 10px;")

        self.load_video_button = QPushButton("Load Video", self)
        self.load_video_button.setStyleSheet("background-color: #2196F3; color: white; border-radius:  15px; padding: 10px;")

        self.translate_button = QPushButton("Translate Text", self)
        self.translate_button.setStyleSheet("background-color: #ff5722; color: white; border-radius: 5px; padding: 10px;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_display)
        layout.addWidget(self.language_selector)
        layout.addWidget(self.load_image_button)
        layout.addWidget(self.load_video_button)
        layout.addWidget(self.translate_button)

        # Container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connections
        self.load_image_button.clicked.connect(self.load_image)
        self.load_video_button.clicked.connect(self.load_video)
        self.translate_button.clicked.connect(self.translate_text)

        # Placeholder variables
        self.extracted_text = ""

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            self.process_image(file_name)

    def load_video(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv)")
        if file_name:
            self.process_video(file_name)

    def process_image(self, file_path):
        image = cv2.imread(file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.extracted_text = pytesseract.image_to_string(gray)

        # Display the image in the label
        qt_image = QImage(image.data, image.shape[1], image.shape[0], image.strides[0], QImage.Format_BGR888)
        self.label.setPixmap(QPixmap.fromImage(qt_image).scaled(self.label.size()*10, Qt.KeepAspectRatio))
        self.text_display.setText(self.extracted_text)
        
# from video extracting
    def process_video(self, file_path):
        cap = cv2.VideoCapture(file_path)
        self.extracted_text = ""

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            self.extracted_text += text

        cap.release()
        self.text_display.setText(self.extracted_text)

    def translate_text(self):
        if not self.extracted_text.strip():
            self.text_display.setText("No text to translate.")
            return

        selected_language = self.language_selector.currentText().split(" ")[0]
        # using deep-translator to translate the text
        translated_text = GoogleTranslator(target=selected_language).translate(self.extracted_text)
        self.text_display.setText(f"Original Text:\n{self.extracted_text}\n\nTranslated Text:\n{translated_text}")


# LAst runing  the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TextTranslateApp()
    main_window.show()
    sys.exit(app.exec_())
