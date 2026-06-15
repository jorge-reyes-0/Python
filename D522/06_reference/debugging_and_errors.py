# D522 - Debugging and Error Types
# Reference notes on Python error categories and common debugging techniques.

# ---------------------------------------------------------------------------
# Error Types
#
# Syntax Errors   — parser can't read the code (typos, missing colons, etc.)
# Runtime Errors  — valid syntax but fails during execution
#                   (e.g., division by zero, missing file, index out of range)
# Semantic Errors — code runs without crashing but produces wrong output
#                   due to logic mistakes (hardest to catch)

# ---------------------------------------------------------------------------
# Debugging Techniques
#
#   print statements  — quick way to inspect variable values mid-execution
#   pdb / debugger    — step through code line by line
#   code review       — a second pair of eyes catches what you miss
#   unit tests        — verify individual functions in isolation
#   logging           — structured output that can be filtered by severity
#   profiling         — find performance bottlenecks

# ---------------------------------------------------------------------------
# Logic Error Example — off-by-one in range()
# range(11) produces 0–10; use range(10) if you only want 0–9.
for i in range(11):
    print(i)

# ---------------------------------------------------------------------------
# Incorrect Boolean Expression
# The intent here is "x is outside the range 0–5".
# `and` requires BOTH conditions to be True simultaneously, which is impossible
# for a single number. Use `or` instead.

x = 3

# Buggy version (always False for any real number):
if x < 0 and x < 5:
    print('x is outside the range 0-5 (WRONG — this condition can never be True)')

# Fixed version:
if x < 0 or x > 5:
    print('x is outside the range 0-5')
else:
    print('x is inside the range 0-5')
