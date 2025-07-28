from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox
from core.imposition import impose_booklet
from utils.logger import log, log_success
from utils.file_utils import open_file

class ImpositionPanel(QWidget):
    def __init__(self, get_pdf_path, go_back, fold_target="A5"):
        super().__init__()
        self.get_pdf_path = get_pdf_path
        self.go_back = go_back
        self.fold_target = fold_target
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        impose_btn = QPushButton(f"Create Booklet ({self.fold_target})")
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
        if not pdf_path or not pdf_path.lower().endswith(".pdf"):
            QMessageBox.warning(self, "Error", "No PDF selected.")
            return

        success, message = impose_booklet(pdf_path, fold_target=self.fold_target)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", f"Failed: {message}")
