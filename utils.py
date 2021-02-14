# coding=utf-8
import re
import warnings
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
warnings.filterwarnings('ignore')
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

def query_url_base(_url, _proxy=True, _isPC=True, _isPhone=False):
    """ 基于requset的模块，不能采集动态网页数据
    :param _url<str>
    :param _proxy<bool>
    :param _isPc<bool>
    :param _isPhone<bool>
    :return _result<dict>
    """
    _result = {}
    _headers = {'Connection':'kepp-alive'}
    if _isPC:
        _headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    elif _isPhone:
        _headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    _ip_url = 'https://restapi.amap.com/v3/ip?output=json&key=880b9655c8c084258bfbedf98145a936'
    _proxy = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080',
    } if _proxy else None
    _pattern_dict = {
        'title': r"<(title|TITLE)>(?P<title>[^<>]+)</(title|TITLE)>"}
    # print(requests.get(_ip_url, proxies=_proxy).json())
    response = requests.post(_url, proxies=_proxy, headers=_headers, verify=False, timeout=30)
    content = response.text
    for k,v in _pattern_dict.items():
        _match = re.search(v, content)
        if not re.match: continue
        _result[k] = _match.groupdict()[k]
    _result['text'] = html2text(content)
    return _result

def html2text(source):
    soup = BeautifulSoup(source, 'lxml')
    result = re.sub(r'(\n|\s|\|)+', ' ', soup.get_text().strip())
    return result

if __name__ == '__main__':
    # 'https://httpbin.org/ip'
    # url_list = ['tTtt','http://www.baidu.com', 'https://www.baidu.com', 'www.baidu.com']
    # for i in url_list:
    #     print(url_dection(i))

    with open('url.txt', 'r') as f:
        url = f.readlines()[8].strip()
    url = url_dection(url)
    for u in url:
        print(u)
        query_url_base(u, _isPC=True)
        query_url_base(u, _isPhone=True)
        break