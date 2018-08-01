# coding=utf-8
import os

# python 函数
#

# def functionname(parameters):
#     "函数_文档字符串"
#     function_suite
#     return [expression]

# def printme(str):
#     "打印传入的字符串到标准显示设备上"
#     print str;
#     return;
#
#
# printme("我需要调用自定义函数")


# 参数传递
# strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

# 不可变对象实例   只是复制该对象
# def changInt(a):
#     a = 10
#
#
# b = 2
# changInt(b)
#
# print b



# 传可变对象实例
# def changeme(list):
#     list.append([1, 2, 3, 4])
#     return list
#
#
# mylist = [10, 20, 30]
# mylist = changeme(mylist)
#
# print mylist



# 文件模块
fo = open("fileTest.txt", "r+")  # w  写入   r读取
# fo.write("python真的很好用哈")
# print fo.name  # 文件名称
# print fo.closed  # 文件是否关闭
# print fo.mode  # 文件模式
# print fo.softspace  # 末尾是否强制加空格
# print fo.read(6)  # 读取字节计数,否则全部读取
#
# fo.seek(0, 0)  # 把指针重新定位到文件开头
# print "指针当前位置", fo.tell()  # 当前位置
# fo.read(6)
# print "指针当前位置", fo.tell()  # 当前位置
#
# fo.close()

os.rename("fileTest.txt", "fileDemo.txt")
