# coding=utf-8
import scrapy
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


#
class itemSpider(scrapy.Spider):
    # 必须和main方法中命令一样
    name = "pachong"
    start_urls = ["http://lab.scrapyd.cn"]

    def parse(self, response):
        pachong = response.css("div.quote")
        print len(pachong)
        for v in pachong:
            text = v.css("div.quote> span.text::text").extract_first()
            author = v.css("span small.author::text").extract_first()
            tags = v.css("div.tags .tag::text").extract()
            tags = "==".join(tags)

            # print text
            # print "作者=========" + author
            # print str(tags).replace('u\'', '\'').decode("unicode-escape")
            # print "tag" + tags
            # 循环提取所有的标题、作者和标签内容
            if author is not None:
                fileName = u'%s-语录.txt' % author
                print fileName
                # fileName = fileName.encode('raw_unicode_escape')
                # fileName = fileName.decode()
            # 文件的名称为作者名字—语录.txt。  # 文件的名称为作者名字—语录.txt。
            if fileName is not None:
                with open("D:\\ideaFile\\python\\NovelCrawler\\NovelCrawler\\anaFile\\" + fileName.decode("utf8"), "a+")as f:
                    if author is not None:
                        f.write('\n-----------------' + author + '---------------------\n')
                    if text is not None:
                        f.write('内容\n' + text)
                    f.write('\n----------------------------------------\n')
                    if tags is not None:
                        f.write('标签\n' + tags)
                    f.write('\n----------------------------------------\n')
                f.close()

        next_page = response.css('li.next a::attr(href)').extract_first()
        print "下一页========"
        next_page = response.urljoin(next_page)
        # time.sleep(0.1)
        yield scrapy.Request(next_page, callback=self.parse)
        # 查看存在不存在下一页的链接，如果存在下一页，把下一页的内容提交给parse然后继续爬取。
        # 如果不存在下一页链接结束爬取。
