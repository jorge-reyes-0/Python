# Debugging and Fixing Errors

# Syntax Errors
    # These occur when the Python parser is unable to understand a line of code.
    # Usually the result of typos or misunderstandings about the syntax.

# Runtime Errors
    # Occur during the execution of a program. Often caused by operations that are
    # mathematically illegal, such as division by zero, or by attempting to access
    # a resource that isnt available, such as reading a file that doesnt exist.

# Semantic Errors
    # These are the most insidious errors as the program runs without crashing, but
    # it doesnt produce the expected output. Could be due to an error in the programs logic

###########################################################################################

# Python Debugging

# Python debugging is a systematic process of finding and reducing the number of bugs or defects
# in a python program.

# Basic steps of python debugging:
    # Understanding the problem
    # Isolating the problem
    # Using a debugger
    # Fixing the error
    # Testing the solution

# Common debugging techniques
    # Print statements
    # Using a debugger
    # Code review
    # Unit testing
    # Logging
    # Profiling

###########################################################################################

# Logic Errors

# Occur when the syntax of the code is correct, but the code does not perform as intended
# due to incorrect logic.

# Example

for i in range(11): # supposed to be 10
    print(i)

# Incorrect Boolean Expressions

# Occur when the conditions in an if statement, while loop or other Boolean expression are not
# correctly formulated. For example, using and instead of or can lead to unexpected results

x = 3

if x < 0 and x < 5:
    print('x is outside the range 0-5')
else:
    print('x is inside the range of 0-5')