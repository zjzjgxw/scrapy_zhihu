# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from zhihu.items import TripadvisorHotelItem


class TripadvisorSpider(CrawlSpider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.cn']
    start_urls = ['https://www.tripadvisor.cn/Hotels']

    rules = (
        Rule(LinkExtractor(allow=r'Hotel_Review*', allow_domains=allowed_domains), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item_loader = ItemLoader(item=TripadvisorHotelItem(), response=response)
        item_loader.add_value('code', response.request.url.split("-")[2])
        item_loader.add_value('url', response.request.url)
        item_loader.add_css('name_cn', "#HEADING::text")
        item_loader.add_css('name_en', "#HEADING .is-hidden-mobile::text")
        item_loader.add_css("rate", "span.ui_bubble_rating::attr(alt)")
        item_loader.add_css("comment_num", "span.reviewCount::text")
        item_loader.add_css("img_url", ".centeredImg::attr(data-lazyurl)")
        return item_loader.load_item()
