import os
import subprocess
import platform

def is_valid_pdf(path):
    return path.lower().endswith(".pdf") and os.path.exists(path)

def get_filename(path):
    return os.path.basename(path)

def get_directory(path):
    return os.path.dirname(path)

def open_file(path):
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.run(["open", path])
        else:
            subprocess.run(["xdg-open", path])
    except Exception as e:
        from utils.logger import log
        log(f" Failed to open file: {e}", level="ERROR")

