from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout

from constructGUI2 import Label

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.label_1 = Label('settings.yml', 'label_1')
        self.label_2 = Label('settings.yml', 'label_2')

        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()