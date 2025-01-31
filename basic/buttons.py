import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton
)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, style_sheet_path: str="") -> None:
        super().__init__()
        
        if style_sheet_path != "":
            self.styling = open(style_sheet_path, "r").read()
        else:
            self.styling = ""

        self.setWindowTitle("Basic GUI")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.initUI()
    
    def initUI(self) -> None:
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        title_label = QLabel("Hello World!")
        title_label.setStyleSheet("background-color: red;")
        self.info1_label = QLabel("Change this number! [0]")
        self.info1_label.setStyleSheet("background-color: blue;")
        info2_label = QLabel(":) (:")
        info2_label.setStyleSheet("background-color: green;")
        
        increase_pushbutton = QPushButton("Increase")
        increase_pushbutton.setStyleSheet("background-color: yellow;")
        increase_pushbutton.clicked.connect(self.on_increase_button_press)
        decrease_pushbutton = QPushButton("Decrease")
        decrease_pushbutton.setStyleSheet("background-color: yellow;")
        decrease_pushbutton.clicked.connect(self.on_decrease_button_press)
        
        grid = QGridLayout()
        grid.addWidget(title_label, 0, 0, 1, 3)
        grid.addWidget(self.info1_label, 1, 0, 1, 2)
        grid.addWidget(info2_label, 1, 2, 2, 1)
        grid.addWidget(increase_pushbutton, 2, 0, 1, 1)
        grid.addWidget(decrease_pushbutton, 2, 1, 1, 1)
        
        main_widget.setLayout(grid)
    
    def on_increase_button_press(self) -> None:
        print("Increased")
        self.info1_label.setText(
            re.sub(
                r"\[[0-9]+\]",
                self.info1_label.text(),
                "[" + str(
                    int(re.findall(
                        r"(?<=\[)[0-9]+(?=\])",
                        self.info1_label.text()
                )[0]) + 1) + "]"
            )
        )

    def on_decrease_button_press(self) -> None:
        print("Decreased")

def main():
    app = QApplication(sys.argv)
    window = MainWindow(style_sheet_path="css/global.css")
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
