from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from core.imposition import impose_2up
from utils.logger import log, log_success
from utils.file_utils import open_file

class ImpositionPanel(QWidget):
    def __init__(self, get_pdf_path, go_back):
        super().__init__()
        self.get_pdf_path = get_pdf_path
        self.go_back = go_back
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        impose_btn = QPushButton("Apply 2-Up Imposition")
        impose_btn.clicked.connect(self.impose)
        layout.addWidget(impose_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)
        impose_btn.setMinimumHeight(35)
        impose_btn.setStyleSheet("font-weight: bold;")

        back_btn.setMinimumHeight(30)
        back_btn.setStyleSheet("color: gray; font-size: 11px;")

    def impose(self):
        pdf_path = self.get_pdf_path()
        if not pdf_path:
            QMessageBox.warning(self, "Error", "No PDF selected.")
            return

        output_path, _ = QFileDialog.getSaveFileName(self, "Save 2-Up PDF", "", "PDF Files (*.pdf)")
        if output_path:
            try:
                impose_2up(pdf_path, output_path)
                log_success(output_path, "2-Up imposed")
                open_file(output_path)
            except Exception as e:
                    log(f"Imposition failed: {e}", level="ERROR")
