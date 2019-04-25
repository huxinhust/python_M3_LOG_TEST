# -*- coding: UTF-8 -*-
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
super_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
normal_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
super_node_id_test = 'Jh4G0VQWXuF9wjlblVsPYXrySBY'
super_node_id='TVfZ-LQn7ZxenP8gsnky-F_J4WM'
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


# print(start_timeStamp)

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
sum_1=0
for i in range(len1):
    if init_data[i]['name'] == 'Download Record':
        len2 = len(init_data[i]['records'])
        for i1 in range(len2):  # 每条日志的所有block
            if init_data[i]['records'][i1]['data']['is_success'] is True:
                if init_data[i]['records'][i1]['data']['end_time'] >= start_timeStamp and \
                        init_data[i]['records'][i1]['data']['start_time'] <= end_timeStamp:
                    sum_1+=1
                    if init_data[i]['records'][i1]['data']['transferred_node_id'] == super_node_id:  # from超级节点
                        # 判断时间段
                        if init_data[i]['records'][i1]['data']['start_time'] < start_timeStamp:
                            if init_data[i]['records'][i1]['data']['end_time'] < end_timeStamp:
                                k1 = panduan_shijianduan(init_data[i]['records'][i1]['data']['end_time'])
                                for i2 in range(0, k1 + 1):
                                    super_count[i2] += 1
                            else:
                                for i3 in range(0, 24):
                                    super_count[i3] += 1
                        else:
                            if init_data[i]['records'][i1]['data']['end_time'] < end_timeStamp:
                                k2 = panduan_shijianduan(init_data[i]['records'][i1]['data']['start_time'])
                                k3 = panduan_shijianduan(init_data[i]['records'][i1]['data']['end_time'])
                                for i4 in range(k2, k3 + 1):
                                    super_count[i4] += 1
                            else:
                                k4 = panduan_shijianduan(init_data[i]['records'][i1]['data']['start_time'])
                                for i5 in range(k4, 24):
                                    super_count[i5] += 1
                    else:  # from普通节点
                        # 判断时间段
                        if init_data[i]['records'][i1]['data']['start_time'] < start_timeStamp:
                            if init_data[i]['records'][i1]['data']['end_time'] < end_timeStamp:
                                k5 = panduan_shijianduan(init_data[i]['records'][i1]['data']['end_time'])
                                for i2 in range(0, k5 + 1):
                                    normal_count[i2] += 1
                            else:
                                for i3 in range(0, 24):
                                    normal_count[i3] += 1
                        else:
                            if init_data[i]['records'][i1]['data']['end_time'] < end_timeStamp:
                                k6 = panduan_shijianduan(init_data[i]['records'][i1]['data']['start_time'])
                                k7 = panduan_shijianduan(init_data[i]['records'][i1]['data']['end_time'])
                                for i4 in range(k6, k7 + 1):
                                    normal_count[i4] += 1
                            else:
                                k8 = panduan_shijianduan(init_data[i]['records'][i1]['data']['start_time'])
                                for i5 in range(k8, 24):
                                    normal_count[i5] += 1

print(super_count)
print(normal_count)
print(sum_1)
plt.figure(1)
ax = subplot(1, 1, 1)
xmajorLocator = MultipleLocator(1)
x = np.arange(24)
str1 = '%s%s%s%s' % (str11, '——', str12, '内，block下载情况')
plt.xticks(x, (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '   21:00', '   22:00', '   23:00'))
plt.title(str1)
plt.xlabel('时间/小时')
plt.ylabel('block数目/个')
plt.bar(x, height=super_count, color='red', label="Super Node", bottom=normal_count)
plt.bar(x, height=normal_count, color='green', label="User Node")
plt.legend()
plt.show()
