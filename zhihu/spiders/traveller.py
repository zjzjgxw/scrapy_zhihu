# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem
from zhihu.settings import COOKIES


class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


class TravellerSpider(scrapy.Spider):
    name = 'traveller'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    # start_urls = ['https://m.weibo.cn/?jumpfrom=wapv4&tip=1']
    cookies = COOKIES  # 带着Cookie向网页发请求
    headers = {
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
    }

    def start_requests(self):
        trans = transCookie(self.cookies)
        cookies = trans.stringToDict()
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, cookies=cookies)  # 这里带着cookie发出请求

    def parse(self, response):
        node_list = response.xpath('//div')
        for node in node_list:
            item = ZhihuItem()
            item['name'] = node.xpath("./a[@class='S_txt1'/@title").extract()
        pass


