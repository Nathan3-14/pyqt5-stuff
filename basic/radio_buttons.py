import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QRadioButton, QButtonGroup
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Basic GUI")
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.suit_buttongroup = QButtonGroup(self)
        self.clubs_radiobutton = QRadioButton("Clubs", self)
        self.hearts_radiobutton = QRadioButton("Hearts", self)
        self.spades_radiobutton = QRadioButton("Spades", self)
        self.diamonds_radiobutton = QRadioButton("Diamonds", self)
        
        self.type_buttongroup = QButtonGroup(self)
        self.face_radiobutton = QRadioButton("Face", self)
        self.number_radiobutton = QRadioButton("Number", self)
        self.initUI()
    
    def initUI(self) -> None:
        self.clubs_radiobutton.setGeometry(0, 0, 300, 40)
        self.hearts_radiobutton.setGeometry(0, 40, 300, 40)
        self.spades_radiobutton.setGeometry(0, 80, 300, 40)
        self.diamonds_radiobutton.setGeometry(0, 120, 300, 40)

        self.suit_buttongroup.addButton(self.clubs_radiobutton)
        self.suit_buttongroup.addButton(self.hearts_radiobutton)
        self.suit_buttongroup.addButton(self.spades_radiobutton)
        self.suit_buttongroup.addButton(self.diamonds_radiobutton)

        self.clubs_radiobutton.toggled.connect(self.radio_button_changed)
        self.hearts_radiobutton.toggled.connect(self.radio_button_changed)
        self.spades_radiobutton.toggled.connect(self.radio_button_changed)
        self.diamonds_radiobutton.toggled.connect(self.radio_button_changed)



        self.face_radiobutton.setGeometry(0, 210, 300, 40)
        self.number_radiobutton.setGeometry(0, 250, 300, 40)

        self.type_buttongroup.addButton(self.face_radiobutton)
        self.type_buttongroup.addButton(self.number_radiobutton)

        self.face_radiobutton.toggled.connect(self.radio_button_changed)
        self.number_radiobutton.toggled.connect(self.radio_button_changed)



        self.setStyleSheet("QRadioButton{font-size: 20px; padding: 10px; font-family: monospace; background-color: darkslategrey; color: white; }")

    def radio_button_changed(self) -> None:
        active_radio_button = self.sender()
        if active_radio_button.isChecked():
            print(f"{active_radio_button.text()} is selected")
    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
