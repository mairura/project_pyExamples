import re

text = "Ted is a full-stack software engineer."
pattern = r"[a-c]"
replacement = "*"

new_text = re.sub(pattern, replacement, text)
print(new_text)
