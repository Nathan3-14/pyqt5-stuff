import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QLineEdit, QPushButton
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Basic GUI")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.fname_enter = QLineEdit(self)
        self.lname_enter = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)
        
        
        self.initUI()
    
    def initUI(self) -> None:
        self.fname_enter.setGeometry(0, 0, 100, 40)
        self.lname_enter.setGeometry(110, 0, 100, 40)
        self.submit_button.setGeometry(160, 0, 50, 30)

        self.setStyleSheet("font-size: 20px;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
