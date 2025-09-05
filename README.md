Log Cleaner

A simple Python tool to analyze and clean log files, focusing on extracting error messages.

✨ Features

Load a log file into memory

Filter lines that contain ERROR

Save extracted errors into a new file

Show a summary (total lines & error lines)

🛠 Requirements

Python 3.x

No external libraries are required (uses only Python standard library).

▶️ Usage
1. Prepare a log file
Make sure you have a log file, e.g. sample.log with lines like:

INFO - Service started
ERROR - Database connection failed
INFO - Retrying...
ERROR - Timeout reached


2. Run the program

python log_cleaner.py


3. Example Output

✅ File sample.log loaded successfully.
🔎 Found 2 error lines.
💾 Errors saved to errors_only.log.
📊 File summary:
   Total lines: 4
   Error lines: 2


. Output Files

sample.log → your input log file

errors_only.log → new file containing only ERROR lines


📂 Project Structure

.
├── log_cleaner.py      # Main code
├── sample.log          # Example input log file
└── README.md           # Project documentation

