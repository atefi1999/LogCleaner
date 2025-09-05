class LogCleaner:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.error_lines = []

    def load_file(self):
        """Read the whole file and store in data"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.data = f.readlines()
            print(f"✅ File {self.filename} loaded successfully.")
        except FileNotFoundError:
            print("❌ File not found.")

    def filter_errors(self):
        """Filter lines that contain ERROR"""
        self.error_lines = [line for line in self.data if "ERROR" in line]
        print(f"🔎 Found {len(self.error_lines)} error lines.")

    def save_errors(self, out_file="errors.log"):
        """Save error lines into a new file"""
        if not self.error_lines:
            print("⚠️ No errors to save.")
            return
        with open(out_file, "w", encoding="utf-8") as f:
            f.writelines(self.error_lines)
        print(f"💾 Errors saved to {out_file}.")

    def summary(self):
        """Show a summary of the file"""
        total = len(self.data)
        errors = len(self.error_lines)
        print("📊 File summary:")
        print(f"   Total lines: {total}")
        print(f"   Error lines: {errors}")


# ---------------- Run the program ----------------
if __name__ == "__main__":
    cleaner = LogCleaner("sample.log")  # log filename
    cleaner.load_file()
    cleaner.filter_errors()
    cleaner.save_errors("errors_only.log")
    cleaner.summary()
