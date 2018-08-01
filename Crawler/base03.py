# coding=utf-8

# 等待用户输入

# raw_input("按下enter键退出,其他任意键显示.....\n")


# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。


# if True:
#     print "fuck"
# else :
#     print "not fuck"


# 变量赋值

# counter = 100  # 整型
# miles = 1000.0  # 浮点型
# name = "瞿亮"  # 字符串
#
# print counter, miles, name


# 多个变量赋值
# a = b = c = 1
#
# print a, b, c
#
# a, b, c, = 1, 2, "瞿亮"
#
# print a, b, c



# 标准数据类型

# Numbaers (数字)
# int（有符号整型）
# long（长整型[也可以代表八进制和十六进制]）
# float（浮点型）
# complex（复数）
#

# String  (字符串)
#
# List    (列表)
#
# Tuple   (元祖)
#
# Dictionary (字典)


# 字符串

# str = "ilovepython"
# print str  # 原型打印出来
# print str[1:5]  # 输出以下标为一的第二个字符开始和以第五个字符结束中的字符串
# print str * 2  # 星号（*）是重复操作
# print str[5:]  # 输出以第五个字符之后的所有字符
# print str + "还不错"  # +连接符

# 列表

# list = ['runoob', 786, 2.23, 70.2]
# tinylist = [123, 'john']
#
# print list  # 输出完整列表
# print list[0]  # 输出第一个元素
# print list[1:3]  # 输出第二个和第三个元素
# print list[2:]  # 输出以下标为二的第三个元素开始之后的所有元素
# print tinylist * 2  # 输出列表两次
# print list + tinylist  # 打印组合的列表


# 元组(以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：)
#
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# list = ['runoob', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000
# list[2] = 1000



# 字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {"name": "john", "code": 6734,
            "dept": "sales"}  # 最好是用单引号来定义元素  {'dept': 'sales', 'code': 6734, 'name': 'john'}
print dict["one"]  # 输出键为one的值
print dict[2]  # 输出键为2的值
print tinydict  # 输出完整字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

