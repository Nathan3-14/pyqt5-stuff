import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QCheckBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Basic GUI")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.title_label = QLabel("Pick any colours you like", self)
        self.red_checkbox = QCheckBox("Red", self)
        self.blue_checkbox = QCheckBox("Blue", self)
        self.green_checkbox = QCheckBox("Green", self)
        
        self.initUI()
    
    def initUI(self) -> None:
        self.title_label.setGeometry(0, 0, 500, 30)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 30px;")

        self.red_checkbox.setGeometry(0, 30, 200, 20)
        self.red_checkbox.setStyleSheet("font-size: 20px;")
        self.red_checkbox.stateChanged.connect(self.checkbox_changed)
        self.blue_checkbox.setGeometry(0, 50, 200, 20)
        self.blue_checkbox.setStyleSheet("font-size: 20px;")
        self.green_checkbox.setGeometry(0, 70, 200, 20)
        self.green_checkbox.setStyleSheet("font-size: 20px;")
    
    def checkbox_changed(self, state: int) -> None:
        if state == Qt.Checked:
            print(f"a checkbox has been ticked")
        else:
            print(f"a checkbox has been unticked")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
