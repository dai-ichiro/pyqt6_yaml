from PyQt6.QtWidgets import *
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