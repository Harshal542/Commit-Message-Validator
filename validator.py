import sys
import re
import tkinter as tk
from tkinter import messagebox

def validate_commit_message(file_path):
    # Read the commit message from the temporary Git file
    with open(file_path, 'r') as file:
        commit_msg = file.read().strip()

    # The Conventional Commits rule
    pattern = r"^(feat|fix|docs|style|refactor|test|chore): .+$"

    # Set up the UI window (hide the main background window)
    root = tk.Tk()
    root.withdraw()
    # Ensure the popup appears on top of all other windows
    root.attributes("-topmost", True) 

    if re.match(pattern, commit_msg):
        # Show a Success GUI Pop-up
        success_msg = f"✅ SUCCESS: Commit Allowed!\n\nMessage: '{commit_msg}'"
        messagebox.showinfo("Git Hook Validator", success_msg)
        sys.exit(0) # 0 means allow the commit
    else:
        # Show an Error GUI Pop-up
        error_msg = (
            "❌ ERROR: Invalid commit message format.\n\n"
            "Format must be: <type>: <description>\n"
            "Types allowed: feat, fix, docs, style, refactor, test, chore\n\n"
            "Example: 'feat: added login page'\n"
            "Your message: '" + commit_msg + "'"
        )
        messagebox.showerror("Git Hook Blocked", error_msg)
        sys.exit(1) # 1 means block the commit

if __name__ == "__main__":
    validate_commit_message(sys.argv[1])