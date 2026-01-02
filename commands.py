import os
import platform
from utils import normalize_path

def pr(text):
    print(text)
    return 0

def list_folder():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            os.system("dir")
        else:
            os.system("ls")
        return 0
    except Exception:
        return 99

def make_folder(name):
    try:
        os.makedirs(name, exist_ok=True)
        print(f"Folder '{name}' created.")
        return 0
    except PermissionError:
        return 4
    except Exception:
        return 99

def re_file(filename):
    try:
        filename = normalize_path(filename)
        os.remove(filename)
        print(f"File '{filename}' removed.")
        return 0
    except FileNotFoundError:
        return 2
    except PermissionError:
        return 4
    except Exception:
        return 99

def install_language(lang_name):
    os_name = platform.system()
    try:
        if os_name == "Windows":
            cmd = f"choco install {lang_name} -y"
        elif os_name == "Linux":
            cmd = f"sudo apt install {lang_name} -y"
        elif os_name == "Darwin":
            cmd = f"brew install {lang_name}"
        else:
            return 99
        print(f"Installing {lang_name} on {os_name}...")
        os.system(cmd)
        print(f"{lang_name} installation completed!")
        return 0
    except Exception:
        return 6
