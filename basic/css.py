import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QPushButton, QWidget, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Basic GUI")
        self.setWindowIcon(QIcon("images/icon.png"))

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        
        self.initUI()
    
    def initUI(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: monospace;
                padding: 10px 50px;
                margin: 10px;
                border: 3px solid;
                border-radius: 10px;
            }
            QPushButton#button1 {
                background-color: #AA0000;
            }
            QPushButton#button1:hover {
                background-color: #CC0000;
            }
            QPushButton#button2 {
                background-color: rgb(25, 77, 51);
            }
            QPushButton#button2:hover {
                background-color: rgb(25, 120, 51);
            }
            QPushButton#button3 {
                background-color: hsl(226, 63%, 31%);
            }
            QPushButton#button3:hover {
                background-color: hsl(226, 63%, 50%);
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
