import re  # A module that to compile a regex pattern that matches valid email address


def val_email(email):
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        print("Valid email address:)")
    else:
        print("Invalid email address!!")


val_email(email="elon@example.com")
# Valid email address:)
val_email(email="allan@gmail.c")  # A test
# Invalid email address!!
val_email(email="elvis@ngeni.io")
# Invalid email address!!
