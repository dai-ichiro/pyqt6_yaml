'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QWidget, QApplication, QSlider, QVBoxLayout, QFrame
from constructGUI import construct

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("sample")

        self.slider_1 = construct(QSlider(), 'settings.yaml', 'slider_1')

        layout = QVBoxLayout()
        layout.addWidget(self.slider_1)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()