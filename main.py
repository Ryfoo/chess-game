from windows.play import *
from windows.options import *
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Title = "Chess Game"
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
        playButton = QPushButton("PLAY")
        optionsButton = QPushButton("OPTIONS")
        playButton.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        optionsButton.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 12px; width: 40px;font-weight: bold;")
        self.layout.addWidget(playButton, 0, 0)
        self.layout.addWidget(optionsButton, 1, 1)
        playButton.clicked.connect(self.chessInit)
        optionsButton.clicked.connect(self.optionsInit)


    def chessInit(self):
        print("play button has been clicked")
        self.close()
        subprocess.run([sys.executable, "windows/play.py"])
        
    def optionsInit(self):
        print("options button has been clicked")
        self.option_window = optionsWindow()
        self.option_window.show()
        self.close()
        




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()