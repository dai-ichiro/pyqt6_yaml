'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from constructGUI import construct

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("sample")

        self.button_1 = construct(QPushButton(), 'settings.yml', 'button_1')
        self.button_2 = construct(QPushButton(), 'settings.yml', 'button_1')

        self.button_1.setStyleSheet(
            "QPushButton {border-radius : 30; border : 2px solid black; background-color: rgb(148, 148, 254)}"
            "QPushButton:pressed {background-color: rgb(100, 100, 232)}"
            )

        self.button_2.setStyleSheet(
            "QPushButton {border-radius : 30; border : 2px solid black; background-color: rgb(254, 254, 100)}"
            "QPushButton:pressed {background-color: rgb(210, 210, 60)}"
            )

        layout = QHBoxLayout()
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()