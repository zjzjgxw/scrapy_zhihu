# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

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


def handle_rate(value):
    tmp = re.search('\d', value).group()
    return tmp


class TripadvisorHotelItem(scrapy.Item):
    # tripadvisor hotel item
    code = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    name_cn = scrapy.Field(output_processor=TakeFirst())
    name_en = scrapy.Field(output_processor=TakeFirst())
    rate = scrapy.Field(input_processor=MapCompose(handle_rate), output_processor=TakeFirst())
    comment_num = scrapy.Field(output_processor=TakeFirst())
    img_url = scrapy.Field(output_processor=TakeFirst())

