# Tayo Shell

Tayo Shell is a **cross-platform command-line shell** designed to run seamlessly on **Windows, Linux, and MacOS** with a simple, consistent syntax.  
It provides beginner-friendly commands, error handling, and scripting support for learning and automation.

---

## 🔹 Features

- **Cross-Platform** – Same commands work on all major OS.
- **Simple Commands** – Easy-to-use commands: `pr`, `list`, `make folder`, `re`, `install`.
- **Error Codes** – Clear feedback with positive, negative, and fatal errors:
  - **0, 2, 4, 6** → Positive (success / actionable)
  - **1, 3, 5** → Negative (user mistakes)
  - **99** → Fatal / unrecoverable
- **Script Support** – Execute scripts with `.tayo` extension.
- **Single Commands File** – All core commands centralized in `commands.py`.
- **Examples Included** – Pre-made example scripts for testing and learning.
- **Unit Tests** – Verify command behavior and error codes with automated tests.

---

## 🔹 Available Commands

| Command | Description | Example |
|---------|------------|---------|
| `pr("text")` | Print text to console | `pr("Hello")` |
| `list` | List folder contents | `list` |
| `make folder <name>` | Create a folder | `make folder my_folder` |
| `re <filename>` | Remove a file | `re file.txt` |
| `install <language>` | Install programming language | `install python` |

---

## 🔹 Example Scripts

### hello.tayo
```tayo
pr("Hello, Tayo Shell!")
