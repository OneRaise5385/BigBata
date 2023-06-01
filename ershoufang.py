import ndc
import pandas as pd
# url
url0 = 'https://zhengzhou.anjuke.com/sale/p'
# 定制请求头
user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'}
# 提取信息
select_name = '.property-content-info-comm-name'
select_address = '.property-content-info-comm-address'
select_tag = '.property-content-info-tag'
select_price = '.property-price-average'
select_url = ''
# 信息初始化
infos = []
# 采集
for i in range(46,50):
    url = url0 + str(i) + '/?from=HomePage_TopBar'
    html = ndc.page_request(url,user_agent)

    name = ndc.page_parse(html,select_name)
    address = ndc.page_parse(html,select_address)
    tag = ndc.page_parse(html,select_tag)
    price = ndc.page_parse(html,select_price)

    for i in range(len(name)):
        infos.append((name[i],address[i][:2],address[i],tag[i],price[i][:-3]))

print(infos)

# 保存到MongoDB中

# 存入csv
name = ['name','address','area','tag','price']
info_csv = pd.DataFrame(columns=name,data=infos)
info_csv.to_csv('info9.csv',encoding='utf-8')


