# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class ZhihuPipeline(object):
    # 初始化
    def __init__(self):
        # 打开数据库连接
        self.db = MySQLdb.connect("localhost", "root", "", "crawler_test")

    # 处理item
    def process_item(self, item, spider):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        # SQL 插入语句
        dic_item = dict(item)
        sql = """INSERT INTO zhihu_user(name,
                    zhihu_id,
                    answer_count,
                    articles_count,
                    avatar_url,
                    url,
                    follower_count)
                    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % \
              (dic_item['username'],
               dic_item['zhihu_id'],
               dic_item['answer_count'],
               dic_item['articles_count'],
               dic_item['avatar_url'],
               dic_item['url'],
               dic_item['follower_count'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except 'db error':
            # Rollback in case there is any error
            self.db.rollback()
        return item

    # 爬虫关闭时
    def close_spider(self, spider):
        self.db.close()
