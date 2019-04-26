# -*- coding: UTF-8 -*-
#图6
import numpy as np
# import demjson
import os
import json
import time
import matplotlib.pyplot as plt
import math
import string
import seaborn as sns
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy import stats
import pandas as pd

fig = plt.figure()
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 初始化
init_data = []
success_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fail_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

start_time0 = '2019-04-24 00:00:00'
end_time0 = '2019-04-25 00:00:00'
timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
start_timeStamp = 1000 * int(time.mktime(timeArray1))
end_timeStamp = 1000 * int(time.mktime(timeArray2))

timestam11 = float(start_timeStamp / 1000)
timeArray11 = time.localtime(timestam11)
str11 = '%s%s%s%s%s%s%s%s' % (
    timeArray11.tm_year, '-', timeArray11.tm_mon, '-', timeArray11.tm_mday, '-', timeArray11.tm_hour, '点')
timestam12 = float(end_timeStamp / 1000)
timeArray12 = time.localtime(timestam12)
str12 = '%s%s%s%s%s%s%s%s' % (
    timeArray12.tm_year, '-', timeArray12.tm_mon, '-', timeArray12.tm_mday, '-', timeArray12.tm_hour, '点')


def panduan_shijianduan(timestamp):
    time1 = (timestamp - start_timeStamp) / 3600000
    kk = math.floor(time1)
    return kk


# 导入日志
fp = open("C://Users/dou/Desktop/新建文件夹/4-24log/4-24log/benchmark-server-standalone1-2019-04-24-1.log", encoding="UTF-8")
for line1 in fp.readlines():
    if line1.startswith('{"name":'):
        init_data.append(json.loads(line1))
len1 = len(init_data)
sum_1 = 0
for i in range(len1):
    if init_data[i]['name'] == 'Download Record':
        len2 = len(init_data[i]['records'])
        if init_data[i]['success'] is True:
            if init_data[i]['endTime'] >= start_timeStamp and \
                    init_data[i]['startTime'] <= end_timeStamp:
                # 判断时间段
                if init_data[i]['startTime'] < start_timeStamp:
                    if init_data[i]['endTime'] < end_timeStamp:
                        k1 = panduan_shijianduan(init_data[i]['endTime'])
                        for i2 in range(0, k1 + 1):
                            success_count[i2] += 1
                    else:
                        for i3 in range(0, 24):
                            success_count[i3] += 1
                else:
                    if init_data[i]['endTime']< end_timeStamp:
                        k2 = panduan_shijianduan(init_data[i]['startTime'])
                        k3 = panduan_shijianduan(init_data[i]['endTime'])
                        for i4 in range(k2, k3 + 1):
                            success_count[i4] += 1
                    else:
                        k4 = panduan_shijianduan(init_data[i]['startTime'])
                        for i5 in range(k4, 24):
                            success_count[i5] += 1
        else:
            if init_data[i]['endTime'] >= start_timeStamp and \
                    init_data[i]['startTime'] <= end_timeStamp:
                # 判断时间段
                if init_data[i]['startTime'] < start_timeStamp:
                    if init_data[i]['endTime'] < end_timeStamp:
                        k1 = panduan_shijianduan(init_data[i]['endTime'])
                        for i2 in range(0, k1 + 1):
                            fail_count[i2] += 1
                    else:
                        for i3 in range(0, 24):
                            fail_count[i3] += 1
                else:
                    if init_data[i]['endTime']< end_timeStamp:
                        k2 = panduan_shijianduan(init_data[i]['startTime'])
                        k3 = panduan_shijianduan(init_data[i]['endTime'])
                        for i4 in range(k2, k3 + 1):
                            fail_count[i4] += 1
                    else:
                        k4 = panduan_shijianduan(init_data[i]['startTime'])
                        for i5 in range(k4, 24):
                            fail_count[i5] += 1
print(success_count)
print(fail_count)

plt.figure(1)  # 图6
ax = subplot(1, 1, 1)
xmajorLocator = MultipleLocator(1)
x = 1 + np.arange(24)

str2 = '%s%s%s%s' % (str11, '——', str12, '内，文件下载情况')
plt.title(str2)
plt.xlabel('时间/小时')
plt.ylabel('次数')
plt.xticks(x, (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '   21:00', '   22:00', '   23:00'))
plt.bar(x, height=success_count, color='green', label="文件下载成功次数")
plt.bar(x, height=fail_count, color='red', label="文件下载失败次数", bottom=success_count)
plt.legend()
plt.show()