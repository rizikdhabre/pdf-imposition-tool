from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog,
    QComboBox, QGroupBox, QHBoxLayout, QFrame
)
from PyQt6.QtGui import QFont
from gui.rotation_panel import RotationPanel
from gui.imposition_panel import ImpositionPanel
from PyQt6.QtCore import Qt
from utils.logger import log, attach_logger
from gui.log_console import LogConsole


class PDFEngine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 Smart PDF Engine")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(720, 500)
        self.logger = LogConsole()
        self.logger.setMaximumHeight(5)

        font=QFont("Segoe UI", 18)
        self.setFont(font)

        self.pdf_path = None
        self.current_operation_widget = None
        self.logger = LogConsole()
        attach_logger(self.logger)

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(10)

        upload_box = QGroupBox("📄 PDF Upload")
        upload_layout = QVBoxLayout()

        self.label = QLabel("Please upload a PDF file to begin.")
        font = QFont("Segoe UI", 20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        upload_layout.addWidget(self.label)

        self.upload_btn = QPushButton("Upload PDF")
        self.upload_btn.setMinimumHeight(40)
        self.upload_btn.clicked.connect(self.upload_pdf)
        upload_layout.addWidget(self.upload_btn)

        upload_box.setLayout(upload_layout)
        main_layout.addWidget(upload_box)

        self.operation_picker = QComboBox()
        self.operation_picker.addItems(["Select Operation", "🌀 Rotate PDF", "📰 2-Up Imposition"])
        self.operation_picker.currentIndexChanged.connect(self.handle_operation_change)
        self.operation_picker.hide()
        self.operation_picker.setMinimumHeight(30)
        main_layout.addWidget(self.operation_picker)

        self.operation_container = QVBoxLayout()
        main_layout.addLayout(self.operation_container)

        self.setLayout(main_layout)
        main_layout.addWidget(self.logger)

    def upload_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdf_path = file_path
            self.label.setText(f"Selected: {file_path}")
            self.operation_picker.show()
            log(f"User uploaded PDF: {file_path}")
        else:
            log("User canceled PDF upload.", level="WARN")

    def get_pdf_path(self):
        return self.pdf_path

    def handle_operation_change(self, index):
        if self.current_operation_widget:
            self.operation_container.removeWidget(self.current_operation_widget)
            self.current_operation_widget.deleteLater()
            self.current_operation_widget = None

        if index == 1:
            self.current_operation_widget = RotationPanel(self.get_pdf_path, self.back_to_main)
        elif index == 2:
            self.current_operation_widget = ImpositionPanel(self.get_pdf_path, self.back_to_main)

        if self.current_operation_widget:
            self.operation_container.addWidget(self.current_operation_widget)

    def back_to_main(self):
        self.operation_picker.setCurrentIndex(0)
        self.operation_picker.hide()
        if self.current_operation_widget:
            self.operation_container.removeWidget(self.current_operation_widget)
            self.current_operation_widget.deleteLater()
            self.current_operation_widget = None
        self.label.setText("Please upload a PDF file to begin.")
