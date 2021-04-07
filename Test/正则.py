import re

content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'

reg = re.compile('\w*o\w*')
x = reg.search(content)
print(x)
print(x.group())
print(x.start())
