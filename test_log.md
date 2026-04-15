# Git Validator Testing Log

# Test 1: Bad Commit (Blocked)
Command run: `git commit -m "added UI script"`
Expected Result: Script blocks the commit and shows an error.
Actual Result: Blocked successfully. ❌
Status: PASS

### Test 2: Good Commit - Feature (Allowed)
Command run: `git commit -m "feat: added UI to the validator"`
Expected Result: Script allows the commit to save.
Actual Result:** Saved successfully. ✅
Status: PASS

Testing completed and verified on local Windows machine.

xyz