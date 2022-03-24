'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtWidgets import QWidget, QApplication, QSlider, QVBoxLayout
from constructGUI import construct

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("sample")

        self.slider_1 = construct(QSlider(), 'settings.yaml', 'slider_1')
        self.slider_2 = construct(QSlider(), 'settings.yaml', 'slider_2')
        self.slider_3 = construct(QSlider(), 'settings.yaml', 'slider_3')
        self.slider_4 = construct(QSlider(), 'settings.yaml', 'slider_4')
        self.slider_5 = construct(QSlider(), 'settings.yaml', 'slider_5')
        self.slider_6 = construct(QSlider(), 'settings.yaml', 'slider_6')
        self.slider_7 = construct(QSlider(), 'settings.yaml', 'slider_7')
        self.slider_8 = construct(QSlider(), 'settings.yaml', 'slider_8')

        layout = QVBoxLayout()
        layout.addWidget(self.slider_1)
        layout.addWidget(self.slider_2)
        layout.addWidget(self.slider_3)
        layout.addWidget(self.slider_4)
        layout.addWidget(self.slider_5)
        layout.addWidget(self.slider_6)
        layout.addWidget(self.slider_7)
        layout.addWidget(self.slider_8)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()