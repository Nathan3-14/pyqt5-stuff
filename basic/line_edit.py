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
        
        self.fname_lineedit = QLineEdit(self)
        self.lname_lineedit = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)
        
        
        self.initUI()
    
    def initUI(self) -> None:
        self.fname_lineedit.setGeometry(0, 0, 100, 40)
        self.fname_lineedit.setPlaceholderText("Name")
        self.lname_lineedit.setGeometry(110, 0, 100, 40)
        self.lname_lineedit.setPlaceholderText("Surname")
        self.submit_button.setGeometry(220, 0, 80, 30)
        self.submit_button.clicked.connect(self.submit)

        self.setStyleSheet("font-size: 20px;")
    
    def submit(self) -> None:
        username = f"{self.fname_lineedit.text()} {self.lname_lineedit.text()}"
        print(username)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
