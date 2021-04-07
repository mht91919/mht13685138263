import requests
import parsel
import csv, time

f = open('租房信息.csv', mode='a', encoding='gbk', newline='')
csc_writer = csv.DictWriter(f, fieldnames=['表题', '基本信息', '地区', '价格'])
csc_writer.writeheader()

for page in range(1, 12):
    time.sleep(1.5)
    url = f'http://cs.ganji.com/zufang/0/pn{page}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

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
        listings = index.css('dl dd:nth-child(5) span span::text').get().strip()  # 房源
        info_href = index.css('.title a::attr(href)').get()  # 连接
        feature = index.css('.feature span::text').get()  # 连接
        price = index.css('.price .num::text').get() + '元/月'  # 价格

        dic = {
            '表题': title,
            '基本信息': info_str,
            '地区': feature,
            '价格': price
        }
        csc_writer.writerow(dic)
