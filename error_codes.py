# Tayo Shell Error Codes
ERROR_CODES = {
    0: ("Success", "Positive"),
    1: ("Unknown command", "Negative"),
    2: ("File not found", "Positive"),
    3: ("Folder not found", "Negative"),
    4: ("Permission denied", "Positive"),
    5: ("Invalid syntax", "Negative"),
    6: ("Install failed", "Positive"),
    99: ("Unknown error", "Negative - Fatal")
}

def handle_error(code):
    """Print error message and exit if fatal"""
    message, etype = ERROR_CODES.get(code, ("Unknown error", "Negative"))
    print(f"Error {code} [{etype}]: {message}")
    if code == 99:
        print("Fatal error encountered. Exiting shell.")
        exit(99)
