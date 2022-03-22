'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QSize
import pickle
import random
from constructGUI import construct

with open('words_dict.pkl', 'rb') as f:
    words_dict = pickle.load(f)

dict_keys = words_dict.keys()

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.question = ''
        self.new_question = True
        
    def initUI(self):
        self.setWindowTitle("単語帳")
        self.setFixedSize(QSize(400, 200))

        self.label_q = construct(QLabel(), 'settings.yaml', 'label_1')
        self.label_a = construct(QLabel(), 'settings.yaml', 'label_1')
        
        layout = QVBoxLayout()
        layout.addWidget(self.label_q)
        layout.addWidget(self.label_a)
        
        self.setLayout(layout)
    
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key.Key_Return:
            if self.new_question == True:
                self.label_a.clear()
                self.question = random.choice(list(dict_keys))
                self.label_q.setText(self.question)
                self.new_question = False
            else:
                self.label_a.setText(', '.join(words_dict[self.question]))
                self.new_question = True

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()