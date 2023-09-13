import requests
from bs4 import BeautifulSoup
import pymongo

def page_request(url, ua):
    '''请求网页'''
    response = requests.get(url, headers=ua)
    html = response.content.decode('utf-8')
    return html

def page_parse(html,select):
    '''解析网页'''
    soup = BeautifulSoup(html,'html.parser')
    content = soup.select(select)
    content_list = []
    for i in range(len(content)):
        content_list.append(content[i].get_text())
    return content_list


def save_mongodb(info_list):
    '''保存到数据库'''
    myclient=pymongo.MongoClient(host='localhost',port=27017)
    mydb=myclient['infos']
    mycol=mydb['info']

    data = {}
    for i in range(len(info_list)):
        data['name'] = info_list[i][0]  # 名称
        data['address'] = info_list[i][1]  # 地址
        data['area'] = info_list[i][2]  # 详细地址
        data['tag'] = info_list[i][3]  #标签
        data['price'] = info_list[i][4]  #价格
        mycol.insert_one(data)
        data = {}

