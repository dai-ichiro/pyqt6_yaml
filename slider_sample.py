from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QSlider, QMainWindow

QSS = """
QSlider::groove:horizontal {
    border: 1px solid;
    height: 10px;
    /*margin: 30px;*/
    background-color: rgb(238, 238, 238);
    /*position: absolute;*/
    left: 50px; right: 50px;
    }
QSlider::handle:horizontal {
    background-color: rgb(80, 80, 232);
    height: 40px;
    width: 40px;
    border-radius: 20px;
    margin: -15px -20px;
    }
QSlider::handle:horizontal:pressed {
    background-color: rgb(148, 148, 254);
}

QSlider::add-page:horizontal {
    background: rgb(183, 183, 183);
}

QSlider::sub-page:horizontal {
    background: rgb(80, 80, 232);
}
"""

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('slider sample')
        #self.setFixedSize(QSize(600,200))
        self.slider_1 = QSlider()
        self.slider_2 = QSlider()

        self.slider_1.setOrientation(Qt.Orientation.Horizontal)
        self.slider_2.setOrientation(Qt.Orientation.Horizontal)

        self.slider_2.setFixedSize(QSize(400,200))
        self.slider_2.setMaximum(10)
        self.slider_2.setMinimum(0)
        self.slider_2.setValue(5)
        self.slider_2.setStyleSheet(QSS)

        
        self.setCentralWidget(self.slider_2)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    ex =Window()
    ex.show()
    app.exec()