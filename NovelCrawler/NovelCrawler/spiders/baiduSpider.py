# coding=utf-8
import scrapy


class baiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://fanyi.baidu.com/translate?aldtype=16047&query=.RemotingException&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/.RemotingException"
    ]

    def parse(self, response):
        fileName = response.url.split("/")[-2]
        print response.css('body')
        open("D:\\ideaFile\\python\\NovelCrawler\\anaFile\\" + fileName, 'w').write(response.body)
