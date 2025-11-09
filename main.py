from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from BookBeats import Ui_BookBeats
# import Api
from gtts import gTTS
import os
import fitz
import threading
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF to Audio File Convert App")
        self.setFixedSize(800, 660)
        self.ui = Ui_BookBeats()
        self.ui.setupUi(self)
        # variable
        file_path = 'Helo'
        self.language = "en"
        self.accent = "us"
        # button action
        self.ui.openfile.clicked.connect(self.open_file)
        self.ui.LanguageList.currentTextChanged.connect(self.select_laguage)
        self.ui.Download.clicked.connect(self.Pdf_into_audio)
        self.ui.linkedin_btn.clicked.connect(self.openLinkedin)
        self.ui.github_btn.clicked.connect(self.openGithub)
   # navbar function

    def openLinkedin(self):
        webbrowser.open("https://www.linkedin.com/in/rajendra-ajay-800150292/")

    def openGithub(self):
        webbrowser.open("https://github.com/RajendraAjay11")
    # pdf open function

    def open_file(self):
        self.ui.openfile.setStyleSheet(u"background-color: red;")
        global file_path
        folder = QFileDialog()
        folder.setFileMode(QFileDialog.ExistingFiles)
        if folder.exec():
            file = folder.selectedFiles()
            path = "".join(file)
            file_path = str(path)
            print("selected file:", file_path)
    # select language

    def select_laguage(self):
        select_lang = self.ui.LanguageList.currentText()
        if select_lang == "Afrikaans":
            self.language = "af"
            print(self.language)
            print(self.accent)
        if select_lang == "Arabic":
            self.language = "ar"
            print(self.language)
            print(self.accent)
        if select_lang == "Bengali":
            self.language = "bn"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Bosnian":
            self.language = "bs"
            print(self.language)
            print(self.accent)
        if select_lang == "Bulgarian":
            self.language = "bg"
            print(self.language)
            print(self.accent)
        if select_lang == "Catalan":
            self.language = "ca"
            print(self.language)
            print(self.accent)
        if select_lang == "Chinese":
            self.language = "zh-CN"
            print(self.language)
            print(self.accent)
        if select_lang == "Croatian":
            self.language = "hr"
            print(self.language)
            print(self.accent)
        if select_lang == "Czech":
            self.language = "cs"
            print(self.language)
            print(self.accent)
        if select_lang == "Danish":
            self.language = "da"
            print(self.language)
            print(self.accent)

        if select_lang == "Dutch":
            self.language = "nl"
            print(self.language)
            print(self.accent)

        if select_lang == "English (Australia)":
            self.language = "en"
            self.accent = "com.au"
            print(self.language)
            print(self.accent)
        if select_lang == "English (India)":
            self.language = "en"
            self.accent = 'co.in'
            print(self.language)
            print(self.accent)
        if select_lang == "English (UK)":
            self.language = "en"
            self.accent = "co.uk"
            print(self.language)
            print(self.accent)

        if select_lang == "English (US)":
            self.language = "en"
            self.accent = "us"
            print(self.language)
            print(self.accent)
        if select_lang == "Filipino":
            self.language = "fil"
            print(self.language)
            print(self.accent)
        if select_lang == "Finnish":
            self.language = "fi"
            print(self.language)
            print(self.accent)
        if select_lang == "French":
            self.language = "fr"
            print(self.language)
            print(self.accent)
        if select_lang == "German":
            self.language = "de"
            print(self.language)
            print(self.accent)
        if select_lang == "Greek":
            self.language = "el"
            print(self.language)
            print(self.accent)
        if select_lang == "Gujarati":
            self.language = "gu"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Hebrew":
            self.language = "he"
            print(self.language)
            print(self.accent)
        if select_lang == "Hungarian":
            self.language = "hu"
            print(self.language)
            print(self.accent)
        if select_lang == "Icelandic":
            self.language = "is"
            print(self.language)
            print(self.accent)
        if select_lang == "Indonesian":
            self.language = "id"
            print(self.language)
            print(self.accent)
        if select_lang == "Italian":
            self.language = "it"
            print(self.language)
            print(self.accent)
        if select_lang == "Japanese":
            self.language = "ja"
            print(self.language)
            print(self.accent)
        if select_lang == "Kannada":
            self.language = "kn"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Javanese":
            self.language = "jv"
            print(self.language)
            print(self.accent)
        if select_lang == "Khmer":
            self.language = "km"
            print(self.language)
            print(self.accent)
        if select_lang == "Korean":
            self.language = "ko"
            print(self.language)
            print(self.accent)
        if select_lang == "Latvian":
            self.language = "lv"
            print(self.language)
            print(self.accent)
        if select_lang == "Lithuanian":
            self.language = "It"
            print(self.language)
            print(self.accent)
        if select_lang == "Malayalam":
            self.language = "ml"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Marathi":
            self.language = "mr"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Nepali":
            self.language = "ne"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Portuguese (Brazil)":
            self.language = "pt"
            self.accent = "com.br"
            print(self.language)
            print(self.accent)
        if select_lang == "Portuguese (Portugal)":
            self.language = "pt"
            self.accent = "pt"
            print(self.language)
            print(self.accent)
        if select_lang == "Punjabi":
            self.language = "pa"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Romanian":
            self.language = "ro"
            print(self.language)
            print(self.accent)
        if select_lang == "Russian":
            self.language = "ru"
            print(self.language)
            print(self.accent)
        if select_lang == "Serbian":
            self.language = "sr"
            print(self.language)
            print(self.accent)
        if select_lang == "Sinhala":
            self.language = "si"
            print(self.language)
            print(self.accent)
        if select_lang == "Slovenian":
            self.language = "sl"
            print(self.language)
            print(self.accent)
        if select_lang == "Spanish":
            self.language = "es"
            self.accent = "es"
            print(self.language)
            print(self.accent)
        if select_lang == "Sundanese":
            self.language = "su"
            print(self.language)
            print(self.accent)
        if select_lang == "Swahili":
            self.language = "sw"
            print(self.language)
            print(self.accent)
        if select_lang == "Swedish":
            self.language = "sv"
            print(self.language)
            print(self.accent)
        if select_lang == "Tamil":
            self.language = "ta"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Telugu":
            self.language = "te"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Thai":
            self.language = "th"
            print(self.language)
            print(self.accent)
        if select_lang == "Turkish":
            self.language = "tr"
            print(self.language)
            print(self.accent)
        if select_lang == "Ukrainian":
            self.language = "uk"
            print(self.language)
            print(self.accent)
        if select_lang == "Urdu":
            self.language = "ur"
            self.accent = "co.in"
            print(self.language)
            print(self.accent)
        if select_lang == "Vietnamese":
            self.language = "vi"
            print(self.language)
            print(self.accent)
        if select_lang == "Welsh":
            self.language = "cy"
            print(self.language)
            print(self.accent)
        if select_lang == "Xhosa":
            self.language = "xh"
            print(self.language)
            print(self.accent)
        if select_lang == "Zulu":
            self.language = "zu"
            print(self.language)
            print(self.accent)

        # convertion function

    def Pdf_into_audio(self):
        reading_text = []
        doc = fitz.open(file_path)
        for i, page in enumerate(doc):
            text = page.get_text()
            reading_text.append(text)
        text = ''''''
        audio_text = text.join(reading_text)
        # print(audio_text)
        myLang = self.language
        tone = self.accent
        # filename
        EnterName = self.ui.audiofilename.text()
        fileName = EnterName+".mp3"
        print(fileName)
        if fileName:
           self.ui.label_7.setText(f"({fileName}) Fill is Downloaded ") 
        # gtts object
        myobj = gTTS(text=audio_text, lang=myLang,
                     slow=False, tld=tone, timeout=None)
        myobj.save(fileName)
        print("Audio File is Downloaded it Play soon...")
        os.system(f"start {fileName}")
    # Run in background thread
    threading.Thread(target=Pdf_into_audio, args=(
        "Hello! This is a test.",)).start()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
