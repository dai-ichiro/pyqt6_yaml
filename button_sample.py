'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/qtyaml.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
from qtyaml import PushButton

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("button sample")

        self.button_1 = PushButton('button_settings.yml', 'button_1')
        self.button_2 = PushButton('button_settings.yml', 'button_1')
        self.button_3 = PushButton('button_settings.yml', 'button_1')

        self.button_4 = PushButton('button_settings.yml', 'button_1')
        self.button_5 = PushButton('button_settings.yml', 'button_1')
        self.button_6 = PushButton('button_settings.yml', 'button_1')

        self.button_7 = PushButton('button_settings.yml', 'circle_button')
        self.button_8 = PushButton('button_settings.yml', 'circle_button')
        self.button_9 = PushButton('button_settings.yml', 'circle_button')

        self.button_10 = PushButton('button_settings.yml', 'circle_button')
        self.button_11 = PushButton('button_settings.yml', 'circle_button')
        self.button_12 = PushButton('button_settings.yml', 'circle_button')

        self.button_1.setStyleSheet(
            "QPushButton {border-radius : 30; border : 2px solid black; background-color: rgb(148, 148, 254)}"
            "QPushButton:pressed {background-color: rgb(100, 100, 232)}")

        self.button_2.setStyleSheet(
            "QPushButton {border-radius : 30; border : 2px solid black; background-color: rgb(254, 254, 100)}"
            "QPushButton:pressed {background-color: rgb(210, 210, 60)}")

        self.button_3.setStyleSheet(
            "QPushButton {border-radius : 30; border : 2px solid black; background-color: rgb(255, 108, 108)}"
            "QPushButton:pressed {background-color: rgb(210, 80, 80)}")
        
        self.button_4.setStyleSheet(
            "QPushButton {border-radius : 30; color: white; background-color: rgb(148, 148, 254)}"
            "QPushButton:pressed {background-color: rgb(100, 100, 232)}")

        self.button_5.setStyleSheet(
            "QPushButton {border-radius : 30; color: white; background-color: rgb(254, 254, 100)}"
            "QPushButton:pressed {background-color: rgb(210, 210, 60)}")

        self.button_6.setStyleSheet(
            "QPushButton {border-radius : 30; color: white; background-color: rgb(255, 108, 108)}"
            "QPushButton:pressed {background-color: rgb(210, 80, 80)}")

        self.button_7.setStyleSheet(
            "QPushButton {border-radius : 75; border : 2px solid black; background-color: rgb(148, 148, 254)}"
            "QPushButton:pressed {background-color: rgb(100, 100, 232)}")
        
        self.button_8.setStyleSheet(
            "QPushButton {border-radius : 75; border : 2px solid black; background-color: rgb(254, 254, 100)}"
            "QPushButton:pressed {background-color: rgb(210, 210, 60)}")
        
        self.button_9.setStyleSheet(
            "QPushButton {border-radius : 75; border : 2px solid black; background-color: rgb(255, 108, 108)}"
            "QPushButton:pressed {background-color: rgb(210, 80, 80)}")
        
        self.button_10.setStyleSheet(
            "QPushButton {border-radius : 75; color: white; background-color: rgb(148, 148, 254)}"
            "QPushButton:pressed {background-color: rgb(100, 100, 232)}")
        
        self.button_11.setStyleSheet(
            "QPushButton {border-radius : 75; color: white; background-color: rgb(254, 254, 100)}"
            "QPushButton:pressed {background-color: rgb(210, 210, 60)}")
        
        self.button_12.setStyleSheet(
            "QPushButton {border-radius : 75; color: white; background-color: rgb(255, 108, 108)}"
            "QPushButton:pressed {background-color: rgb(210, 80, 80)}")

        layout = QGridLayout()
        layout.addWidget(self.button_1, 0, 0, 1, 1)
        layout.addWidget(self.button_2, 0, 1, 1, 1)
        layout.addWidget(self.button_3, 0, 2, 1, 1)

        layout.addWidget(self.button_4, 1, 0, 1, 1)
        layout.addWidget(self.button_5, 1, 1, 1, 1)
        layout.addWidget(self.button_6, 1, 2, 1, 1)

        layout.addWidget(self.button_7, 2, 0, 1, 1, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button_8, 2, 1, 1, 1, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button_9, 2, 2, 1, 1, alignment = Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.button_10, 3, 0, 1, 1, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button_11, 3, 1, 1, 1, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button_12, 3, 2, 1, 1, alignment = Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()