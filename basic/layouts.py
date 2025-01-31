import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
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
        info1_label = QLabel("Check out this cool ui!")
        info1_label.setStyleSheet("background-color: blue;")
        info2_label = QLabel(":) (:")
        info2_label.setStyleSheet("background-color: green;")
        info3_label = QLabel("Wow, so cool!")
        info3_label.setStyleSheet("background-color: yellow;")
        # image_label = QLabel()
        # image_label.pixmap = QPixmap("images/icon.png")
        # image_label.setScaledContents(True)
        
        grid = QGridLayout()
        grid.addWidget(title_label, 0, 0, 1, 2)
        grid.addWidget(info1_label, 1, 0, 1, 1)
        grid.addWidget(info2_label, 1, 1, 2, 1)
        grid.addWidget(info3_label, 2, 0, 1, 1)
        # vbox.addWidget(image_label)
        
        main_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow(style_sheet_path="css/global.css")
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
