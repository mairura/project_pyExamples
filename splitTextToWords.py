import re

re.split(r'\s+', 'ab  c')

re.split(r'[\s\,]+', 'a,b, c  d')
# ['a', 'b', 'c', 'd']

re.split(r'[\s\,\;]+', 'a,b;; c  d')
# ['a', 'b', 'c', 'd']
