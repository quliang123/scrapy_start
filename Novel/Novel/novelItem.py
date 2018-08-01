# coding=utf-8
import scrapy


class novelItem(scrapy.Item):
    bookName = scrapy.Field()
    content = scrapy.Field()
    createTime = scrapy.Field()
