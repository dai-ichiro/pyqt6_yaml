'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QFrame, QSlider
from constructGUI import construct

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("sample")

        self.label_1 = construct(QLabel(), 'settings.yaml', 'label_1')
        self.label_2 = construct(QLabel(), 'settings.yaml', 'label_2')
        self.slider_1 = construct(QSlider(), 'settings.yaml', 'slider_1')

        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.slider_1)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()