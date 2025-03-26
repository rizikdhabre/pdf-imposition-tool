from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class LogConsole(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setStyleSheet("background-color: #111; color: #0f0; font-family: monospace;")
        layout.addWidget(self.text_area)
        self.setLayout(layout)

    def log(self, message):
        self.text_area.append(message)
