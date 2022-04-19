from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout

from constructGUI2 import Slider

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.slider_1 = Slider("settings.yml", "slider_1")
        self.slider_2 = Slider("settings.yml", "slider_2")

        layout = QVBoxLayout()
        layout.addWidget(self.slider_1)
        layout.addWidget(self.slider_2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()