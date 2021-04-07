import requests
import parsel

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
url = 'http://cs.ganji.com/zufang/'

response = requests.get(url=url, headers=headers)

selector = parsel.Selector(response.text)

divs = selector.css('.f-list div.ershoufang-list')

for index in divs:
    title = index.css('.title a::text').get()
    info_list = index.css('.size span::text').getall()
    # 列表转str
    info_str = ','.join(info_list)
    info_address = index.css('.area a span::text').get()
    # dl下的dd模块 第5个
    listings = index.css('dl>dd:nth-child(5) span span::text').get()
    info_href = index.css('.title a::attr(href)').get()
    print(info_str, info_address, info_href, sep='/')
    break
