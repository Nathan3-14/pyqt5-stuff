import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QLabel, QVBoxLayout
)
from PyQt5.QtCore import (
    QTimer, QTime, Qt
)
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        
        self.initUI()
    
    def initUI(self) -> None:
        self.setWindowTitle("Clock")
        self.setGeometry(700, 500, 300, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        # Styling
        self.time_label.setStyleSheet("font-size: 150px; color: #00BBFA;")
        self.setStyleSheet("background-color: darkslategrey;")
        font_id = QFontDatabase.addApplicationFont("digitfont.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        digit_font = QFont(font_family, 150)
        self.time_label.setFont(digit_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()
    
    def update_time(self) -> None:
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
