import re

# Using sub() function


def remove_special_characters(input_string):
    # Use regex to remove special characters
    return re.sub('[^A-Za-z0-9]+', '', input_string)


# Test the function
original_string = 'Hello! How are you? #today'
clean_string = remove_special_characters(original_string)
print(f"Original String: {original_string}")
print(f"Clean String: {clean_string}")
