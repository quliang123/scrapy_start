# coding=utf-8

#  python 循环语句

# 1、while循环
# while   if   else

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = []
# odd = []
#
# while len(numbers) > 0:
#     number = numbers.pop()  # 把列表中的元素从后取出来
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
#
# print even
# print odd




# if number % 2 == 0:
#     even.append(number)
# else:
#     odd.append(number)  # print even
# print odd

# count = 0
# while (count < 9):
#     print 'The count is:', count
#     count = count + 1
#
# print "Good bye!"


# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:
#         continue
#         print i
#
# i = 1
# while 1:
#     print i
#     i += 1
#     if i > 10:
#         print i
#         break


# while else
# count = 0
# while count < 5:
#     print  count
#     count += 1
# else:  # 条件不满足,就走这
#     print "等于五", count



# for 循环

# # 遍历字符串
# for var in "python":
#     print var
#
# # 遍历列表
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:
#     print fruit

# 遍历数字
#
# for i in range(1, 21):  # range  生成x,y-1的列表
#     print i


# 通过序列索引迭代

# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print '第', index+1, '种水果,名字是' + fruits[index]


# 循环使用else
# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print '%d 等于 %d * %d' % (num, i, j)
#             break
#     else:
#         print num



# 打印直角三角形

# rows = int(raw_input("输入列数:"))
#
# for i in range(0, rows):
#     for j in range(0,i):
#         print '*',
#         j += 1
#     i -= 1
#     print "\n"


# 循环字符串
# for v in 'python':
#     if v == 'h':
#         break
#     print v

# for letter in 'Python':
#     if letter == 'h':
#         pass
#         print '这是 pass 块'
#     print '当前字母 :', letter
