from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QListWidget, QListView
from music import Ui_MusicApp  # import the converted class
import os
import sys
import time
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import Qt, QTimer
from io import BytesIO
import pygame
import webbrowser
from pygame import mixer
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller path
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon_path = resource_path("icons/icon.png")


class MainWindow(QMainWindow):
    pygame.init()
    mixer.init()

    def __init__(self):
        super().__init__()
        self.setFixedSize(955, 628)
        self.setWindowIcon(QIcon(resource_path("icons/icon.png")))
        self.ui = Ui_MusicApp()
        self.ui.setupUi(self)  # setup the UI
        self.ui.linkedln.setOpenExternalLinks(False)

        # when linkedln clicked open link
        self.ui.linkedln.mousePressEvent = self.open_linkedln
        self.ui.github.setOpenExternalLinks(False)
        self.ui.github.mousePressEvent = self.open_github
        # when github clicked open link
        self.ui.open_btn.clicked.connect(self.open_file)
        self.ui.play_btn.clicked.connect(self.upause)
        self.ui.paush_btn.clicked.connect(self.pause)
        self.ui.vol_dec_btn.clicked.connect(self.vol_dec)
        self.ui.vol_inc_btn_2.clicked.connect(self.vol_inc)
        self.ui.next_btn.clicked.connect(self.next_play)
        self.ui.prev_btn.clicked.connect(self.prev_play)
        self.ui.audio_list.itemClicked.connect(self.play_track)

    def open_linkedln(self, event):
        webbrowser.open('www.linkedin.com/in/rajendra-ajay-800150292')

    def open_github(self, event):
        webbrowser.open('https://github.com/RajendraAjay11')

    def open_file(self):
        global list_dict
        list_dict = {}
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        if file:
            self.ui.audio_list.clear()
            for filename in os.listdir(file):
                filepath = os.path.join(file, filename)
                if os.path.isfile(filepath):  # Only list files
                    self.ui.audio_list.addItem(filename)
                    list_dict[filename] = filepath

    def play_track(self):
        selected = self.ui.audio_list.currentItem()
        audio = str(selected.text())
        track = list_dict.get(audio)
        mixer.music.load(str(track))
        mixer.music.play()
        self.current_playing()
        self.load_cover()
        self.duration_bar(track)

        music_end = pygame.USEREVENT+1
        mixer.music.set_endevent(music_end)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    mixer.music.stop()
                elif event.type == music_end:
                    self.next_play()

    def pause(self):
        mixer.music.pause()

    def upause(self):
        mixer.music.unpause()

    def vol_inc(self):
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)

    def vol_dec(self):
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)

    def next_play(self):
        index = self.ui.audio_list.currentRow()
        index += 1
        next = self.ui.audio_list.item(index).text()
        self.ui.audio_list.setCurrentRow(index)
        track = list_dict.get(next)
        mixer.music.load(str(track))
        mixer.music.play()
        self.current_playing()
        self.load_cover()
        self.duration_bar(track)

    def prev_play(self):
        index = self.ui.audio_list.currentRow()
        index -= 1
        next = self.ui.audio_list.item(index).text()
        self.ui.audio_list.setCurrentRow(index)
        track = list_dict.get(next)
        mixer.music.load(str(track))
        mixer.music.play()
        self.current_playing()
        self.load_cover()
        self.duration_bar(track)

    def current_playing(self):
        current = self.ui.audio_list.currentItem()
        current_text = current.text()
        self.ui.current_track.setText(current_text)

    def load_cover(self):
        selected = self.ui.audio_list.currentItem()
        audio = str(selected.text())
        track = list_dict.get(audio)
        file_path = track
        if not file_path:
            return

        try:
            audio = MP3(file_path, ID3=ID3)
            for tag in audio.tags.values():
                if isinstance(tag, APIC):  # Image tag
                    image_data = tag.data
                    image = QImage.fromData(image_data)
                    pixmap = QPixmap.fromImage(image)
                    self.ui.cover_img.setPixmap(pixmap.scaled(
                        300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    return

                self.ui.cover_img.setText("No cover image found.")
        except Exception as e:
            self.ui.cover_img.setText(f"Error: {str(e)}")

    def duration_bar(self, track):
        audio = MP3(track)
        total_sec = audio.info.length
        print(total_sec)
        second = round(total_sec)
        second = int(second)
        self.ui.timebar.setMaximum(second)
        playing = True
        while playing:
            for x in range(second+1):
                self.ui.timebar.setValue(x)
                time.sleep(1)
                if x == second:
                    self.ui.timebar.setValue(0)
                    playing = False

    def duration_bar(self, track):
        audio = MP3(track)
        total_sec = int(audio.info.length)
        self.ui.timebar.setMaximum(total_sec)
        self.current_time = 0

        # Stop existing timer if any
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()

            # Create a new timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)  # every second

    def update_progress(self):
        if self.current_time <= self.ui.timebar.maximum():
            self.ui.timebar.setValue(self.current_time)
            self.current_time += 1
        else:
            self.timer.stop()
            self.ui.timebar.setValue(0)
            self.current_time = 0


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
