import re


def extract_numbers(text):
    pattern = r"\d+"  # Used to match a number in regex
    return re.findall(pattern, text)


print(extract_numbers("There are over 1000000 views of Ted's Articles"))
