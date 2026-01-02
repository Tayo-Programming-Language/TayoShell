import os
import platform

def get_os_name():
    """Return the current OS name: Windows, Linux, or Darwin (MacOS)"""
    return platform.system()

def normalize_path(path):
    """Normalize file path to be cross-platform"""
    return os.path.normpath(path)

def command_exists(cmd):
    """Check if a command exists in system PATH"""
    from shutil import which
    return which(cmd) is not None
