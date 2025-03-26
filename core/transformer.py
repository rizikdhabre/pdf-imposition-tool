import fitz  # PyMuPDF

def rotate_pdf(input_path, output_path, angle):
    try:
        doc = fitz.open(input_path)
        for page in doc:
            page.set_rotation(angle)
        doc.save(output_path)
        doc.close()
        return True, "PDF updated successfully."
    except Exception as e:
        return False, str(e)
