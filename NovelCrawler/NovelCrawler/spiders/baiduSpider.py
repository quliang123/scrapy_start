# coding=utf-8
import scrapy


class baiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "https://www.baidu.com/"
    ]

    def parse(self, response):
        fileName = response.url.split("/")[-2] + ".txt"
        print response.body
        open("D:\\ideaFile\\python\\NovelCrawler\\NovelCrawler\\anaFile\\" + fileName, 'a+').write(response.body)
