# gui/secondary_window.py
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout

class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secondary Window")
        
        # Layout and label
        layout = QVBoxLayout()
        label = QLabel("This is the secondary window.")
        layout.addWidget(label)
        self.setLayout(layout)
