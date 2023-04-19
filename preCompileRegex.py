import re
re_numbers = re.compile(r'^\d+$')
print(re_numbers.match('123'))
# <re.Match object; span=(0, 3), match='123'>
print(re_numbers.match('Yang'))
# None
