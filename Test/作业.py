import requests
from lxml import etree


url = 'https://m.lianjia.com/xz/loupan/'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

response = requests.get(url=url, headers=headers)

html = response.text

mytree = etree.HTML(html)

title = mytree.xpath('/html/head/title/text()')


print(html)
