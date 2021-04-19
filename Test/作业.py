# http://travel.qunar.com/travelbook/list.htm?page=1&order=hot_heat
# http://travel.qunar.com/youji/

import requests
import parsel
import time
import random
from lxml import etree

urlbase = 'http://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}


def baseurl_fun():
    for i in range(1, 10):
        url = urlbase.format(i + 1)

        resource = requests.get(url=url, headers=headers)
        selector = parsel.Selector(resource.text)

        uls = selector.css('.b_strategy_list .list_item')

        info_href = uls.css('h2 a::attr(href)').get()  # 连接

        break

        # for j in uls:
        #     info_href = j.css('h2 a::attr(href)').get()  # 连接
        #     print(info_href)
        #     break

        time.sleep(random.randint(1, 2))

    return info_href


def spider():
    href = baseurl_fun()

    resource = requests.get(f'http://travel.qunar.com{href}', headers=headers)

    resource.encoding = "utf-8"

    html = resource.text

    root = etree.HTML(html)

    selector = parsel.Selector(resource.text)

    ul = selector.css('.foreword_list')

    when = ul.css('.when p::text').get().strip()
    whens = ul.css('.when p span:nth-child(2)::text').get().strip()

    howlong = ul.css('.howlong p::text').get().strip()
    howmuch = ul.css('.howlong p span:nth-child(2)::text').get().strip()

    print(href, whens, howmuch)


if __name__ == '__main__':
    spider()
