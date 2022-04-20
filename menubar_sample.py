from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication,QLabel,QMainWindow
from PyQt6.QtGui import QAction

from collections import OrderedDict

menu_list = OrderedDict(
    ファイル = ['新規', '保存', '終了'],
    編集 = ['切り取り', 'コピー', '貼り付け', '全選択'],
    ヘルプ = ['バージョン情報']
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(400,300))
        self.label = QLabel()
        self.setCentralWidget(self.label)

        self.menubar = self.menuBar()
        self.menu = []
        self.action = []
        for key, val in menu_list.items():
            
            self.menu.append(self.menubar.addMenu(key))

            for submenu in val:
                self.action.append(QAction(submenu))
                self.menu[-1].addAction(self.action[-1])
                self.action[-1].triggered.connect(lambda state, x=submenu: self.menubarAction(x))
            
    def menubarAction(self, menu_name: str) -> None:
        self.label.setText(f'You pushed {menu_name}!')

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()