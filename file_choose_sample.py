'''
import os
from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/dai-ichiro/pyqt6_yaml/main/constructGUI.py'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    urlretrieve(url, fname)
'''
from PyQt6 import QtCore
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QFileDialog
from constructGUI import construct

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("pyQt6 sample")

        self.img_label = construct(QLabel(), 'settings.yaml', 'label_1')
        self.button1 = construct(QPushButton(), 'settings.yaml', 'button_1')
        
        layout = QVBoxLayout()
        layout.addWidget(self.img_label)
        layout.addWidget(self.button1)
        
        self.setLayout(layout)

        self.button1.clicked.connect(self.showDialog1)
    
    def showDialog1(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file')

        # fname[0]は選択したファイルのパス（ファイル名を含む）
        if fname[0]:
            # 画像の読み込み, サイズ変更
            image = QImage(fname[0]).scaled(512,512,QtCore.Qt.AspectRatioMode.KeepAspectRatio) 
            # 画像の表示
            self.img_label.setPixmap(QPixmap.fromImage(image))

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()