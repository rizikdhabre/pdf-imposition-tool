from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QFileDialog, QMessageBox
from core.transformer import rotate_pdf
from utils.logger import log, log_success
from utils.file_utils import open_file

class RotationPanel(QWidget):
    def __init__(self, get_pdf_path, go_back):
        super().__init__()
        self.get_pdf_path = get_pdf_path
        self.go_back = go_back
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Select rotation angle:"))

        self.angle_selector = QComboBox()
        self.angle_selector.addItems(["90", "180", "270"])
        layout.addWidget(self.angle_selector)

        rotate_btn = QPushButton("Rotate and Save")
        rotate_btn.clicked.connect(self.rotate_pdf)
        layout.addWidget(rotate_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)
        rotate_btn.setMinimumHeight(35)
        rotate_btn.setStyleSheet("font-weight: bold;")

        back_btn.setMinimumHeight(30)
        back_btn.setStyleSheet("color: gray; font-size: 11px;")
        layout.setSpacing(15)
        layout.setContentsMargins(10, 10, 10, 10)

    def rotate_pdf(self):
        pdf_path = self.get_pdf_path()
        if not pdf_path:
            QMessageBox.warning(self, "Error", "No PDF selected.")
            return

        angle = int(self.angle_selector.currentText())
        output_path, _ = QFileDialog.getSaveFileName(self, "Save Rotated PDF", "", "PDF Files (*.pdf)")
        if output_path:
            success, message = rotate_pdf(pdf_path, output_path, angle)
            if success:
                log_success(output_path, f"rotated by {angle}°")
                open_file(output_path)
            else:
                log(message, level="ERROR")
