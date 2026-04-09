import sys
import re

def validate_commit_message(file_path):
    
    with open(file_path, 'r') as file:
        commit_msg = file.read().strip()

    pattern = r"^(feat|fix|docs|style|refactor|test|chore): .+$"

    if re.match(pattern, commit_msg):
        print("\n✅ SUCCESS: Commit message validated!")
        sys.exit(0) 
    else:
        print("\n❌ ERROR: Invalid commit message format.")
        print("Format must be: <type>: <description>")
        print("Types allowed: feat, fix, docs, style, refactor, test, chore")
        print("Example: 'feat: added login page' or 'fix: resolved crash'\n")
        sys.exit(1) 

if __name__ == "__main__":
    validate_commit_message(sys.argv[1])