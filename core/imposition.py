import os
from typing import Tuple, Optional
import fitz  # PyMuPDF

from utils.logger import log_success, log_error
from utils.pdf_tools import plan_signatures, panel_count, build_folded_panel_order


def impose_booklet(input_pdf_path: str, fold_target: str = "A5", output_path: Optional[str] = None) -> Tuple[bool, str]:
    try:
        if not os.path.exists(input_pdf_path):
            return False, f"Input file not found: {input_pdf_path}"

        doc = fitz.open(input_pdf_path)
        n_pages = len(doc)
        print(f"📄 Loaded PDF with {n_pages} pages.")

        # Plan layout
        signatures, blanks = plan_signatures(n_pages)
        print(f"🧩 Planned signatures: {signatures}")
        print(f"📦 Blank pages needed: {blanks}")

        panels_per_sheet = panel_count(fold_target)
        print(f"📐 Fold target '{fold_target}' → {panels_per_sheet} panels per A4 sheet")

        panel_order, added_blanks = build_folded_panel_order(n_pages, fold_target)
        print(f"📋 Final panel order: {panel_order}")

    except Exception as e:
        log_error(f"Booklet imposition failed: {e}")
        return False, str(e)

