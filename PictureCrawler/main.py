# coding=utf-8
import sys

from scrapy import cmdline

reload(sys)
sys.setdefaultencoding('utf8')

# list = [1, 2, 3, 4, 5, 6,7]
# print list[-2]

# str = "http://img1.mm131.me/pic/4163/1.jpg"
# i = 0
# print '%d' % i + "." + str.split("/")[-1].split(".")[-1]




# def writePic(path):
#     # 判断路径是否存在
#     # 存在     True
#     # 不存在   False
#     # isExists = os.path.exists(path)
#
#     # 判断结果
#     if not os.path.exists(path):
#         # 如果不存在则创建目录
#         # 创建目录操作函数
#         os.makedirs(path)
#         print path + ' 创建成功'
#         return True
#     else:  # 如果目录存在则不创建，并提示目录已存在
#         print path + ' 目录已存在'
#         return False


# writePic("D:\\ideaFile\\python\\PictureCrawler\\imageFile\\美女图片\\性感美女\\宅男女神王")

# path = "D:\\ideaFile\\python\\PictureCrawler\\imageFile\\美女图片\\性感美女\\宅男女神王".decode('utf-8')

# if not os.path.exists(path):
#     print "222"
#     os.makedirs(path, 0)

# urllib.urlretrieve("http://img1.mm131.me/pic/4144/1.jpg", path + "\\1.jpg")

# print "http://img1.mm131.me/pic/4160/1.jpg".split("/")[-1]

# s="我是一个人(中国人)aaa[真的]bbbb{确定}"
# a = re.sub(u"\\(.*?\\)|\\{.*?}", "", s)
#
# print a

# a = [u'\u9999\u8273\u5c11\u5987\u5c24\u59ae\u4e1d\u53cc\u5cf0\u9971\u6ee1\u64a9\u4eba\u5fc3\u9b42']

# print a[-1]


# print "hh/1.png".split('/')[-1].split('.')[-2]

cmdline.execute("scrapy crawl PictureCrawler".split())
