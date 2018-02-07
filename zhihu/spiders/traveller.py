# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem
from zhihu.settings import COOKIES
import json


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
    start_urls = ['https://www.zhihu.com/api/v4/topics/19551556/followers?include=data%5B%2A%5D.gender%2Canswer_count%2Carticles_count%2Cfollower_count%2Cis_following%2Cis_followed&limit=20&offset=10020']
    cookies = COOKIES  # 带着Cookie向网页发请求

    def start_requests(self):
        trans = transCookie(self.cookies)
        cookies = trans.stringToDict()
        yield scrapy.Request(url=self.start_urls[0], cookies=cookies)  # 这里带着cookie发出请求

    def parse(self, response):
        node_list = json.loads(response.body)['data']
        for node in node_list:
            item = ZhihuItem()
            item['username'] = node['name']
            item['answer_count'] = node['answer_count']
            item['articles_count'] = node['articles_count']
            item['avatar_url'] = node['avatar_url']
            item['follower_count'] = node['follower_count']
            item['url'] = node['url']
            item['zhihu_id'] = node['id']
            yield item
        next_page = json.loads(response.body)['paging']['next']
        url = next_page.replace("http", "https")
        trans = transCookie(self.cookies)
        cookies = trans.stringToDict()
        if next_page:
            yield scrapy.Request(url, cookies=cookies)

