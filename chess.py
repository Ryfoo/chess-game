import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.setGeometry(0, 0, 600, 600)
        self.setWindowIcon(QIcon("chess_logo.png"))
        self.initUI()

    def show(self):
        print("Window is shown")
        super().show()
    
    def initUI(self):
        central_layout = QWidget()
        self.setCentralWidget(central_layout)
        grid_layout = QGridLayout()
        self.labels = []
        for row in range(8):
            for col in range(8):
                label = QLabel(self)
                label.setFixedSize(70, 70)
                
                if (row + col) % 2 == 0:
                    label.setStyleSheet("background-color: #f0d9b5;")
                else:
                    label.setStyleSheet("background-color: #b58863;")
                
                grid_layout.addWidget(label, row, col)
                self.labels.append(label)

        central_layout.setLayout(grid_layout)

        self.board_state - self.initialize_board()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()