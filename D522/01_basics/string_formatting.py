# D522 - String Formatting
# Covers: .format() placeholders, index-based args, positional args,
#         number formatting, and padding / alignment.

# ---------------------------------------------------------------------------
# Basic placeholder substitution
name = "Jorge"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

# ---------------------------------------------------------------------------
# Index-based formatting — explicitly reference argument positions
index_msg = "{0} is a {1} programming language.".format("Python", "versatile")
print(index_msg)

# ---------------------------------------------------------------------------
# Positional arguments — useful for invoices, reports, etc.
product = "Laptop"
price = 1200.50
invoice = "Product: {}, Price: ${}".format(product, price)
print(invoice)

# ---------------------------------------------------------------------------
# Number formatting — thousand separator and two decimal places
value = 1234567.89
formatted_value = "Formatted value: {:,.2f}".format(value)
print(formatted_value)

# ---------------------------------------------------------------------------
# Padding and alignment
# >  right-align   <  left-align   ^  center-align
# The number after the symbol is the total field width.
text = "Python"
right_aligned  = "{:>10}".format(text)   # "    Python"
left_aligned   = "{:<10}".format(text)   # "Python    "
center_aligned = "{:^10}".format(text)   # "  Python  "
print(repr(right_aligned))
print(repr(left_aligned))
print(repr(center_aligned))
