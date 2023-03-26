# Define a function to check length of passsword is strong enough
def password_checker(password):
    # Define the criteria fro a strong password
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"

    # Check the length of the password
    if len(password) < min_length:
        print("Password is too short!")
        return False
    # Check if the password contains an uppercase letter, lowercase letter, digit and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    # Print an error message for each missing criteria
    if not has_uppercase:
        print("Password must contain atleast one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain atleast one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain atleast one digit")
        return False
    if not has_special_char:
        print("Password must contain atleast one special character")
        return False

    # If criteria is met, print success message
    print("Password is strong!")
    return True


# Prompt user to enter a password and check if it meets the criteria
password = input("Enter a password:")
password_checker(password)
