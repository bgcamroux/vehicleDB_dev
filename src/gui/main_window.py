# gui/main_window.py

from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from gui.secondary_window import SecondaryWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Layout and button to open secondary window
        self.layout = QVBoxLayout()
        self.open_button = QPushButton("Open Secondary Window")
        self.open_button.clicked.connect(self.open_secondary_window)

        self.layout.addWidget(self.open_button)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def open_secondary_window(self):
        self.secondary_window = SecondaryWindow()
        self.secondary_window.show()
