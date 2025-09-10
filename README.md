# Log Cleaner

A simple Python tool to **analyze and clean log files** by extracting error messages.

---

## ✨ Features
- Load a log file into memory
- Detect and extract lines containing `ERROR`
- Save extracted errors into a new file
- Display a summary (total lines and error lines)

---

## 🛠 Requirements
- Python 3.x

> No external libraries are needed — only Python standard library.

---

## ▶️ Usage

### 1. Prepare a log file
Example `sample.log`:
```markdown
INFO - Service started
ERROR - Database connection failed
INFO - Retrying...
ERROR - Timeout reached
```

### 2. Run the program
```bash
python log_cleaner.py
```

### 3. Example Output
```markdown
✅ File sample.log loaded successfully.
🔎 Found 2 error lines.
💾 Errors saved to errors_only.log.
📊 File summary:
   Total lines: 4
   Error lines: 2
```

### 4. Output Files
```markdown
sample.log → Input log file

errors_only.log → File containing only extracted error lines
```
---
## 📂 Project Structure
```backtick
.
├── log_cleaner.py      # Main program
├── sample.log          # Example input log file
└── README.md           # Project documentation
```

