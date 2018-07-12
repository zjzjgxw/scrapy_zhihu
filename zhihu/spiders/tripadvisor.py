# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TripadvisorSpider(CrawlSpider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.cn']
    start_urls = ['https://www.tripadvisor.cn/Hotels']

    rules = (
        Rule(LinkExtractor(allow=r'Hotel_Review*', allow_domains=allowed_domains), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        return i
