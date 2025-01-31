import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, style_sheet_path: str="") -> None:
        super().__init__()
        
        if style_sheet_path != "":
            styling = open(style_sheet_path, "r").read()
        else:
            styling = ""

        self.setWindowTitle("Basic GUI")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))


        title_label = QLabel("Hello World!", self)
        title_label.setFont(QFont("Helvetica", 30))
        title_label.setGeometry(0, 0, 500, 50)
        title_label.setStyleSheet(" ".join(styling.split("\n")))
        title_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        image_label = QLabel(self)
        image_pixmap = QPixmap("images/scene.png")
        
        image_label.setGeometry(0, 50, 200, 50)
        image_label.setScaledContents(True)
        image_label.setPixmap(image_pixmap)
        image_label.setGeometry(
            (self.width() - image_label.width()) // 2,
            60,
            image_label.width(),
            image_label.height()
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow(style_sheet_path="css/global.css")
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
