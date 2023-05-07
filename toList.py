import re


def convert_string_to_list(string):
    return string.split(',')


string = "apple,banana,cherry,date"
print(convert_string_to_list(string))

# Case 2


def convert_string_to_list(string):
    return [x.strip() for x in string.split(',')]


string = "apple,banana,cherry,date"
print(convert_string_to_list(string))

# Case 3


def convert_string_to_list(string):
    return re.split(r'\s*,\s*', string)


string = "apple, banana, cherry, date"
print(convert_string_to_list(string))
