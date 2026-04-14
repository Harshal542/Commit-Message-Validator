import os

hook_dir = ".git/hooks"
hook_file = os.path.join(hook_dir, "commit-msg")

if not os.path.exists(hook_dir):
    print("❌ ERROR: Not a Git repository. Run 'git init' first.")
else:
    with open(hook_file, "w") as f:
        f.write("#!/bin/sh\npython validator.py \"$1\"\n")
    print("✅ SUCCESS: Git commit validator installed perfectly!")