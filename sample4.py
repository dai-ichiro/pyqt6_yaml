from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout

from constructGUI2 import PushButton

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.button_1 = PushButton('settings.yml', 'button_1')
        self.button_2 = PushButton('settings.yml', 'circle_button')

        layout = QVBoxLayout()
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()