import requests
import parsel
import re
import fileOp


# 列表url，请求
# 获取每一篇的url
# 请求
# 获取标题内容
# 保存数据html
# html转pdf

def init():
    url = 'https://blog.csdn.net/xiaohuoche175/category_7961113.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    response = requests.get(url=url, headers=headers)
    # selector  对象

    selector = parsel.Selector(response.text)

    href = selector.css('.blog_main .column_list .clearfix span a::attr(href)').getall()
    return headers, href


def changetitle(title):
    mode = re.compile(r'[\/\\\:\*\"\<\>\|\：]')
    new_title = re.sub(mode, '', title)
    return new_title


def scarpy(html_str):
    (headers, href) = init()
    print(href)
    for i in href:
        response_detail = requests.get(url=i, headers=headers).text
        selector_detail = parsel.Selector(response_detail)
        title = selector_detail.css('#articleContentId::text').get().strip()
        new_title = changetitle(title)
        content = selector_detail.css('#content_views').get()
        html = html_str.format(article=content)
        html_filename = 'PDF\\' + new_title + '.html'

        fileOp.FileOp.savefile(filename=html_filename, note=html)


def main():
    html_str = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
    {article}
    </body>
    </html>
    '''
    scarpy(html_str)


if __name__ == '__main__':
    main()
