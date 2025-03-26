import sys
from PyQt6.QtWidgets import QApplication
from gui import PDFEngine

def load_stylesheet(path):
    with open(path, "r") as file:
        return file.read()

def main():
    app = QApplication(sys.argv)

    stylesheet = load_stylesheet("styles/light.qss")
    app.setStyleSheet(stylesheet)

    window = PDFEngine()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
