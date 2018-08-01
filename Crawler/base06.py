# coding=utf-8
import time;
import calendar;

# 时间日期
#
# 时间戳

# ticks = time.time()
#
# print ticks



# 当前时间

localTime = time.localtime(time.time())

# 获取格式化时间

# farmatTime = time.asctime(time.localtime(time.time()))
#
# print localTime
#
# print farmatTime

# 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# # 格式化成Tue May 01 19:10:49 2018形式
# print time.strftime("%a %b %d %H:%M:%S %Y")
#
# # 将字符串转换成时间戳 Tue May 01 19:10:49 2018
# a = "Tue May 01 19:10:49 2018"
# print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))


# 获取某某年的某月的日历

cal = calendar.month(2016, 1)
print cal


