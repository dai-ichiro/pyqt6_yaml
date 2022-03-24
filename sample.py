'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QFrame
from constructGUI import construct

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("sample")

        self.label_1 = construct(QLabel(), 'settings.yaml', 'label_1')
        self.label_2 = construct(QLabel(), 'settings.yaml', 'label_2')
        self.label_3 = construct(QLabel(), 'settings.yaml', 'label_3')
        self.label_4 = construct(QLabel(), 'settings.yaml', 'label_4')
        self.label_5 = construct(QLabel(), 'settings.yaml', 'label_5')
        self.label_6 = construct(QLabel(), 'settings.yaml', 'label_6')
        self.label_7 = construct(QLabel(), 'settings.yaml', 'label_7')

        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.label_3)
        layout.addWidget(self.label_4)
        layout.addWidget(self.label_5)
        layout.addWidget(self.label_6)
        layout.addWidget(self.label_7)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()