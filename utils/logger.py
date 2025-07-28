from datetime import datetime
from utils.file_utils import get_filename, get_directory

_log_console = None

def attach_logger(console_widget):
    global _log_console
    _log_console = console_widget

def log(message, level="INFO"):
    now = datetime.now().strftime("%H:%M:%S")
    formatted = f"[{now}] [{level}] {message}"
    if _log_console:
        _log_console.log(formatted)
    else:
        print(formatted)

def log_success(file_path, operation):
    file_name = get_filename(file_path)
    directory = get_directory(file_path)

    message = (
        f"File \"{file_name}\" was successfully {operation}.\n"
        f"Saved at: {directory}\n"
    )

    log(message, level="INFO")
    
def log_error(message: str) -> None:
    """
    Shortcut used by core.imposition to write ERROR-level entries.
    """
    log(message, level="ERROR")