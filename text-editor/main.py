from fileinput import filename
import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPlainTextEdit,
    QFileDialog,
    QPushButton,
    QGridLayout, QVBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.save_dialogue = None
        self.open_dialogue = None
        
        self.setWindowTitle("Text Editor")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.currentfile = ""
        self.title_label = QLabel("unnamed")
        self.text_plaintext = QPlainTextEdit()
        self.action_buttons_layout = QVBoxLayout()
        self.save_pushbutton = QPushButton("Save")
        self.open_pushbutton = QPushButton("Open")
        self.dialog = QFileDialog()
        
        self.initUI()
    
    def initUI(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.title_label.setStyleSheet("font-size: 20px;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.save_pushbutton.setObjectName("save-button")
        self.save_pushbutton.pressed.connect(self.save_file)
        self.open_pushbutton.setObjectName("open-button")
        self.open_pushbutton.pressed.connect(self.open_file)

        self.action_buttons_layout.addWidget(self.save_pushbutton)
        self.action_buttons_layout.addWidget(self.open_pushbutton)
        
        grid = QGridLayout()
        grid.addWidget(self.title_label, 0, 0, 1, 2)
        grid.addLayout(self.action_buttons_layout, 0, 2, 1, 1)
        grid.addWidget(self.text_plaintext, 1, 0, 3, 3)
        
        central_widget.setLayout(grid)
    
    def save_file(self) -> None:
        if self.currentfile != "":
            file_name = self.currentfile
        else:
            self.dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            self.dialog.show()
            
            while not self.dialog.exec_():
                pass
            file_name = self.dialog.selectedFiles()[0]
        
        print(f"Saving file to '{file_name}'")
        with open(file_name, "w") as f:
            f.write(self.text_plaintext.toPlainText())

    def open_file(self) -> None:
        self.dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.dialog.show()
        
        while not self.dialog.exec_():
            pass
        file_name = self.dialog.selectedFiles()[0]
        
        print(f"Opening file '{file_name}'")
        self.currentfile = file_name
        self.title_label.setText(file_name.split("/")[-1])
        with open(file_name, "r") as f:
            self.text_plaintext.appendPlainText(f.read())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
