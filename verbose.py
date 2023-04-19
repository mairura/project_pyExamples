import re

text = "Yang, yang@example.com, 555-555-5555"
pattern = r"""(?P<name>\w+), \s(?P<email>\w+@\w+\.\w+), \s(?P<phone>\d{3}-\d{3}-\d{4})"""
match = re.search(pattern, text, re.VERBOSE)
if match:
    print(match.group("name"))
    print(match.group("email"))
    print(match.group("phone"))

# We can write a long regular expression into multiple lines for better readability. As long as there is a re.VERBOSE flag in the re.search() function, it can be recognized correctly as usual.
