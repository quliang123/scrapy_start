# coding=utf-8

# python 运算符


# 1、 python算术运算符
#
# a, b = 10, 20
#
# print a + b  # 加
# print a - b  # 减
# print a * b  # 乘
# print a / b  # 除
# print a % b  # 取模
# print a ** b  # 幂   返回a的b次幂
# print a // b  # 取整除  返回商的整数部分


# 2、python比较运算符

# a, b = 10, 20
#
# print a == b  # 等于
# print a != b  # 不相等
# print a <> b  # 不相等,类似!=
# print a > b  # 大于
# print a < b  # 小于
# print a >= b  # 大于等于
# print a <= b  # 小于等于



# 3、python赋值运算符
# a, b = 10, 20
#
# c = a + b  # 赋值 将a+b赋值给c
# print c
#
# a += b  # 等价于a=a+b
# print a
#
# a -= b  # 等价于a-a-b
# print a
#
# a *= b  # 等价于a=a*b
# print a
#
# a /= b  # 等价于a=a*b
# print a
#
# a %= b  # 等价于a=a%b
# print a
#
# a **= b  # 等价于a=a**b
# print a
#
# a //= b  # 等价于a=a//b
# print a


# 4、python位运算符
# a, b, c = 60, 13, 0
#
# # a, b = 00111100, 00001101
# c = a & b  # 12 = 0000 1100
# print c
#
# c = a | b  # 61 = 0011 1101
# print c
#
# c = a ^ b  # 49 = 0011 0001
# print c
#
# c = ~a  # -61 = 1100 0011
# print c
#
# c = a << 2  # 240=1111 0000
# print c
#
# c = a >> 2  # 15=0000 1111
# print c



# 5、python逻辑运算符
#
# a, b = 10, 20
#
# # 与
# print a and b  # 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
#
# # 或
# print a or b  # 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
#
# # 非
# print not a and b  # 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。


# 6、python成员运算符
# list = [1, 2, 3, 4, 5]
#
# print 1 in list
#
# print 2 not in list


# 7、python身份运算符
# is 与 == 区别：

# a, b = 20, 20
#
# print a is b, a == b  # 等价于 a == b
#
# print a is not b, a != b  # 等价于a != b
#
# # is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
# a = [1, 2, 3]
# b = a
# print b is a
#
# b = a[:]  # 复制
# print b is a
#
# print b == a
#
# b = a  # 重新引用地址
#
# print b is a
