import sys
import re

def validate_commit_message(file_path):
    # Read the commit message from the temporary Git file
    with open(file_path, 'r') as file:
        commit_msg = file.read().strip()

    # Rule: Must start with feat:, fix:, docs:, style:, refactor:, test:, or chore:
    pattern = r"^(feat|fix|docs|style|refactor|test|chore): .+$"

    if re.match(pattern, commit_msg):
        print("\n✅ SUCCESS: Commit message validated!")
        sys.exit(0) # 0 means the commit is allowed to proceed
    else:
        print("\n❌ ERROR: Invalid commit message format.")
        print("Format must be: <type>: <description>")
        print("Types allowed: feat, fix, docs, style, refactor, test, chore")
        print("Example: 'feat: added login page' or 'fix: resolved crash'\n")
        sys.exit(1) # 1 means the commit is blocked

if __name__ == "__main__":
    # sys.argv[1] is the file path Git passes to the script
    validate_commit_message(sys.argv[1])