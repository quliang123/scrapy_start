# coding=utf-8
from lxml import etree

from scrapy.selector import Selector
from scrapy.spiders import crawl
from scrapy.http import Request, response
from Novel.Novel.items import novelItem
import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class NovelSpider(scrapy.Spider):
    name = "Novel"
    start_urls = ["https://www.booktxt.net/0_790/"]
    offset = 0

    # 分别请求某个分类下的部分或者是(全部文章)
    def parse(self, response):

        selector = Selector(response)
        # // dl // dt / following - sibling:: *
        infos = response.xpath("//dl//dd/a/@href").extract()
        # print infos

        for v in infos:
            try:
                # print v
                response = scrapy.Request("https://www.booktxt.net/0_790/" + v, dont_filter=True,
                                          callback=self.parse_Item)

                yield response
                # item[''] = v.xpath('')
                # yield item
            except IndexError:
                pass
                # yield scrapy.Request(next_page, callback=self.parse)  # 分别请求某篇小说下的所有文章  # 分别请求某篇小说下的所有文章

    # 剥取小说的所有章节
    def parse_Item(self, response):
        # print response.css("div .box_con").extract()
        # print str(response.css("div.box_con").extract()).replace('u\'', '\'').decode("unicode-escape")

        # 获取具体文章大体,再依次获取标题,内容
        for n in response.css("div.box_con"):
            bookName = n.xpath("//h1/text()").extract_first()
            print bookName
            # print n.xpath("//div[@id='content']/text()").extract()
            # print n.replace('u\'', '\'').decode("UTF-8").css("h1")

            # 获取当前文章内容
            for content in n.xpath("//div[@id='content']/text()").extract():
                # print y + "\n"
                if bookName is not None:
                    fileName = u'%s-语录.txt' % bookName
                # 保存文件
                with open("D:\\ideaFile\\python\\Novel\\NovelFile\\" + fileName, "a+") as f:
                    if bookName is None:
                        f.write(bookName + "\n")
                    if content is not None:
                        f.write(content + "\n")
                    f.close()
