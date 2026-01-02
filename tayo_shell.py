from commands import pr, list_folder, make_folder, re_file, install_language
from error_codes import ERROR_CODES, handle_error

while True:
    cmd = input("tayo> ").strip()
    error_code = 0

    if cmd.startswith("pr(") and cmd.endswith(")"):
        text = cmd[3:-1].strip('"\'')
        error_code = pr(text)
    elif cmd == "list":
        error_code = list_folder()
    elif cmd.startswith("make folder "):
        name = cmd[len("make folder "):].strip()
        error_code = make_folder(name)
    elif cmd.startswith("re "):
        filename = cmd[len("re "):].strip()
        error_code = re_file(filename)
    elif cmd.startswith("install "):
        lang = cmd[len("install "):].strip()
        error_code = install_language(lang)
    elif cmd == "exit":
        break
    else:
        error_code = 1  # Unknown command

    if error_code != 0:
        handle_error(error_code)
