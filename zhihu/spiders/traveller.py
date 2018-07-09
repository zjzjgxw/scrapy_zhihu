# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem
import json

from scrapy.http.cookies import CookieJar    # 该模块继承自内置的http.cookiejar,操作类似


class TravellerSpider(scrapy.Spider):
    name = 'traveller'
    allowed_domains = ['zhihu.com']
    headers = {
        'Host':
            'www.zhihu.com',
        'Connection':
            'keep-alive',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    }

    cookie_jar = CookieJar()

    loginUrl = 'https://www.zhihu.com/#signin'
    siginUrl = 'https://www.zhihu.com/login/email'

    start_urls = ['https://www.zhihu.com/api/v4/topics/19551556/followers?include=data%5B%2A%5D.gender%2Canswer_count%2Carticles_count%2Cfollower_count%2Cis_following%2Cis_followed&limit=20&offset=10020']

    def start_requests(self):
        return [
            scrapy.http.FormRequest(
                self.loginUrl,
                headers=self.headers,
                callback=self.post_login)
        ]

    def post_login(self, response):
        self.cookie_jar.extract_cookies(response,response.request)
        xsrf = response.xpath("//input[@name='_xsrf']/@value").extract_first()
        self.headers['X-Xsrftoken'] = xsrf
        return [
            scrapy.http.FormRequest(
                self.siginUrl,
                method='POST',
                headers=self.headers,
                meta={'cookiejar': response.meta['cookiejar']},
                formdata={
                    '_xsrf': xsrf,
                    'captcha_type': 'cn',
                    'email': 'xxxxxx@163.com',
                    'password': 'xxxxxx',
                },
                callback=self.after_login)
        ]

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

