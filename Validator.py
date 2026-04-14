import sys
import re
import tkinter as tk
from tkinter import messagebox

def validate_commit_message(file_path):
   
    with open(file_path, 'r') as file:
        commit_msg = file.read().strip()

   
    pattern = r"^(feat|fix|docs|style|refactor|test|chore): .+$"

    
    root = tk.Tk()
    root.withdraw()
   
    root.attributes("-topmost", True) 

    if re.match(pattern, commit_msg):
       
        success_msg = f"✅ SUCCESS: Commit Allowed!\n\nMessage: '{commit_msg}'"
        messagebox.showinfo("Git Hook Validator", success_msg)
        sys.exit(0) # 0 means allow the commit
    else:
       
        error_msg = (
            "❌ ERROR: Invalid commit message format.\n\n"
            "Format must be: <type>: <description>\n"
            "Types allowed: feat, fix, docs, style, refactor, test, chore\n\n"
            "Example: 'feat: added login page'\n"
            "Your message: '" + commit_msg + "'"
        )
        messagebox.showerror("Git Hook Blocked", error_msg)
        sys.exit(1) # 1 means block the commit

if _name_ == "_main_":
    validate_commit_message(sys.argv[1])
