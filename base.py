import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Basic GUI")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.helloworld_label = QLabel("Hello World!", self)
        
        self.initUI()
    
    def initUI(self) -> None:
        self.helloworld_label.setGeometry(0, 0, 500, 30)
        self.helloworld_label.setAlignment(Qt.AlignCenter)
        self.helloworld_label.setStyleSheet("font-size: 30px;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
