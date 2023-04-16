import re


def is_valid_phone_number(phone_number):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone_number))


print(is_valid_phone_number("123-456-7890"))  # True
print(is_valid_phone_number("1234567890"))  # False
print(is_valid_phone_number("07-01234567"))  # True
