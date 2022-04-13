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

        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.label_3)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()