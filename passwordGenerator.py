import random
import string
"""This function generates a random password
    of a given length using a combination of
    uppercase letters, lowercase letters,
    digits, and special characters"""

# A string with all possible combinations


def generate_password(length):

    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a password using a random selection of characters
    password = "".join(random.choice(all_chars) for i in range(length))

    return password


password = generate_password(10)
print(password)
