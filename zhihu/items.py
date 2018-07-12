# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    avatar_url = scrapy.Field()
    follower_count = scrapy.Field()
    url = scrapy.Field()
    zhihu_id = scrapy.Field()


class TripadvisorHotelItem(scrapy.Item):
    # tripadvisor hotel item
    code = scrapy.Field()
    url = scrapy.Field()
    name_cn = scrapy.Field()
    name_en = scrapy.Field()
    rate = scrapy.Field()
    comment_num = scrapy.Field()
    rank_describe = scrapy.Field()
    img_url = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    hotel_url = scrapy.Field()
    star = scrapy.Field()

