# coding=utf-8
import scrapy
import sys
import urllib
import os
import re
# from PictureCrawler.items import ImageItem
from ..items import ImageItem

reload(sys)
sys.setdefaultencoding('utf8')


class pictureSpider(scrapy.Spider):
    name = "PictureCrawler"
    allowed_domains = ["www.mm131.com"]
    start_urls = ["http://www.mm131.com/xinggan/"]

    # 解析整个美女图片类型
    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}  # cookie = {

        pic_urls = response.xpath(
            "//dl[contains(@class, 'list-left public-box')]//dd[not(@class='page')]/a/@href").extract()
        #

        next_page = response.xpath("//a[contains(@class, 'page-en')]/@href").extract()

        for pic_url in pic_urls:
            # print "一级url"
            yield scrapy.Request(pic_url, callback=self.parse_Item, headers=headers)
            # if next_page is not None and next_page[-2] is not None:
            #     print "下一组照片"
            #     yield response.follow("http://www.mm131.com/xinggan/" + next_page[-2],
            #                           callback=self.parse, headers=headers)

    def parse_Item(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

        # Cookie = {
        #     'Cookie': 'UM_distinctid=164a0d259a61c7-01f49250f564e6-7b113d-144000-164a0d259a7669; bdshare_firstime=1531706497483; CNZZDATA3866066=cnzz_eid%3D1606495341-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1531796699,1531837934,1531838010,1531913594; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1531913601'}

        print response.url + "进来了" + str(response.status)

        # print response.body
        topics = response.xpath(
            "//div[contains(@class, 'place')]/a//text()").extract()

        picGroup = response.xpath("//div[contains(@class, 'content')]//h5//text()").extract()

        try:
            if topics is not None and len(topics) > 0:
                img_url = response.xpath(
                    "//div[contains(@class,'content-pic')]/a/img/@src").extract()
                # print img_url
                # file_path = "D:\\ideaFile\\python\\PictureCrawler\\imageFile\\" + "%s\\%s\\%s" % (
                #     topics[0], topics[1], re.sub(u"\\(.*?\\)|\\{.*?}", "", picGroup[-1]))

                file_name = str(img_url[-1]).split("/")[-1]

                # img_url = '%d' % i + "." + img_Info.split("/")[-1].split(".")[-1]
                # print img_url
                # print file_path + "=====\n" + img_url[-1] + "=======\n" + str(img_url[-1]).split("/")[-1]

                file_path = list("%s" % (re.sub(u"\\(.*?\\)|\\{.*?}", "", picGroup[-1])))
                # for x in file_path:
                #     print x

            # print file_path[-1] + "===file_path"+"".join(file_path)
            item = ImageItem()
            item['image_urls'] = img_url
            item['referer'] = response.url
            item['file_path'] = file_path
            yield item

        finally:  # //div[contains(@class,'content-page')]//a[contains(@class, 'page-ch')][2]/@href
            next_pic = response.xpath("//div[@class='content-page']//a[@class='page-ch']/@href").extract()
            if next_pic is not None and len(next_pic) > 0:
                # print "下一页" + next_pic[-1] + "数据"
                yield scrapy.Request(url="http://www.mm131.com/xinggan/" + next_pic[-1],
                                     callback=self.parse_Item, headers=headers)  # , cookies=Cookie
