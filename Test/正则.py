# import re
#
# content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
#
# reg = re.compile('\w*o\w*')
# x = reg.search(content)
# print(x)
# print(x.group())
# print(x.start())

import re


# 定义一个函数来对匹配结果进行展示
def display_match_obj(match_obj):
    if match_obj is None:
        print('Regex Match Fail!')
    else:
        print('Regex Match Success!', match_obj)



# if __name__ == '__main__':
#     p = re.compile(r'[a-z]+')
#     display_match_obj(p.match('hello'))
#     display_match_obj(p.match('hello123'))
#     display_match_obj(p.fullmatch('hello'))
#     display_match_obj(p.fullmatch('hello123'))
#     display_match_obj(p.match('123hello'))
#     display_match_obj(p.match('123hello',pos=3,endpos=5))#第3位开始

if __name__ == '__main__':
    p=re.compile(r'[a-z]+')
    display_match_obj(re.match(p,'123hello'[3:]))  # 先切割str，再用模块级的函数