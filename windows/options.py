import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QVBoxLayout,QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor, QPalette  
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class optionsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Title = "Options"
        self.Height, self.Width = 800 , 800
        self.layout = QGridLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)
        self.setStyleSheet("""
            QWidget {
                background-image: url('assets/mainBackground.png');
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        self.initUI()
    

    def initUI(self):
        self.setWindowTitle(self.Title)
        #adjust x and y as needed
        self.setGeometry(600, 150, self.Height, self.Width)
        sound = QPushButton("SOUND")
        theme = QPushButton("THEME")
        profile = QPushButton("PROFILE")
        back = QPushButton("BACK TO MAIN MENU")
        exit = QPushButton("EXIT")
        sound.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        theme.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        profile.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        back.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        exit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        
        
        self.layout.addWidget(sound)
        self.layout.addWidget(theme)
        self.layout.addWidget(profile)
        self.layout.addWidget(back)
        self.layout.addWidget(exit)

        exit.clicked.connect(self.exitFun)

    @pyqtSlot()
    def exitFun(self):
            self.close()


