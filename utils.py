# coding=utf-8
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
""" 
TODO 
    （1）获取网页的所有请求
1、检验
2、补全，尝试HTTP或HTTPS
3、是否添加代理访问
4、手机端与PC端分别访问
5、获取网站标题、TEXT信息
6、对TEXT词频、TF-IDF获取关键词
"""

def url_dection(_url):
    """ URL清洗，并添加前缀
    :param url<str>
    :return [url<str>,...]
    """
    prefix = ['http://', 'https://']
    http_pattern = re.compile(r'^http(s)?://') 
    assert isinstance(_url, str), 'url param type is {}'.format(type(_url))
    _url = _url.replace(' ', '')
    if not http_pattern.match(_url):
        return [_p+_url for _p in prefix]
    else:
        return [_url]

def query_url_base(_url, _proxy=False):
    _proxy = {
        'http': 'http://127.0.0.1:1080',
        'https': 'http://127.0.0.1:1080',
    } if _proxy else None 
    response = requests.get('https://httpbin.org/ip', proxies=_proxy)
    print(response.json())

if __name__ == '__main__':
    # url_list = ['tTtt','http://www.baidu.com', 'https://www.baidu.com', 'www.baidu.com']
    # for i in url_list:
    #     print(url_dection(i))
    query_url_base('s')