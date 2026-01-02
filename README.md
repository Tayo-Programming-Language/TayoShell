# Tayo Shell

Tayo Shell သည် **cross-platform command-line shell** ဖြစ်ပြီး Windows, Linux, MacOS အားလုံးမှာ တူညီသော syntax ဖြင့် commands ကို run နိုင်ပါသည်။  

### 🔹 Features
- Cross-platform commands: `pr`, `list`, `make folder`, `re`, `install`
- Positive / Negative / Fatal error codes
- Scripts with `.tayo` extension
- Simple, beginner-friendly syntax
- Single `commands.py` file for all core commands
- Examples included: `hello.tayo`, `folder_test.tayo`, `install_example.tayo`
- Unit tests in `tests/` folder

### 🔹 Commands

| Command | Description | Example |
|---------|------------|---------|
| `pr("text")` | Print text | `pr("Hello")` |
| `list` | List folder contents | `list` |
| `make folder <name>` | Create folder | `make folder test` |
| `re <filename>` | Remove file | `re file.txt` |
| `install <language>` | Install programming language | `install python` |

### 🔹 Error Codes

| Code | Meaning | Type |
|------|--------|------|
| 0 | Success | Positive |
| 2 | File not found | Positive |
| 4 | Permission denied | Positive |
| 6 | Install failed | Positive |
| 1 | Unknown command | Negative |
| 3 | Folder not found | Negative |
| 5 | Invalid syntax | Negative |
| 99 | Unknown error (Fatal) | Negative |

### 🔹 Usage

1. Clone repository:
```bash
git clone https://github.com/tayo-programming-language/tayo-shell.git
cd tayo-shell
