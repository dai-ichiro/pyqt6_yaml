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

        self.start_button = construct(QPushButton(), 'settings.yaml', 'button_1')
        self.end_button = construct(QPushButton(), 'settings.yaml', 'button_2')
        
        layout = QHBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.end_button)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()