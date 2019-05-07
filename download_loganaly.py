# -*- coding: UTF-8 -*-
# 图1和图3和图2和图8
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
download_time = []
block_dict = {}
super_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
normal_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
from_cache = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
super_count_PR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
normal_count_PR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
from_cache_PR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
super_node_id_test = 'Jh4G0VQWXuF9wjlblVsPYXrySBY'
super_node_id = 'TVfZ-LQn7ZxenP8gsnky-F_J4WM'
start_time0 = '2019-05-06 00:00:00'
end_time0 = '2019-05-07 00:00:00'
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
fp = open("C://Users/dou/Desktop/1/benchmark-server-standalone1-2019-05-06-1.log", encoding="UTF-8")
for line1 in fp.readlines():
    if line1.startswith('{"name":'):
        init_data.append(json.loads(line1))
len1 = len(init_data)
sum_1 = 0
for i in range(len1):
    if init_data[i]['name'] == 'Download Record':
        len2 = len(init_data[i]['records'])
        if init_data[i]['nodeId'] not in block_dict:  # 图3
            block_dict[init_data[i]['nodeId']] = 0
        for i1 in range(len2):  # 每条日志的所有block
            if init_data[i]['records'][i1]['data']['is_success'] is True:
                if init_data[i]['records'][i1]['data']['end_time'] >= start_timeStamp and \
                        init_data[i]['records'][i1]['data']['start_time'] <= end_timeStamp:
                    block_dict[init_data[i]['nodeId']] += 1
                    download_time.append((init_data[i]['records'][i1]['data']['end_time'] -
                                          init_data[i]['records'][i1]['data']['start_time']) / 1000)
                    sum_1 += 1
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
                                    if init_data[i]['records'][i1]['data']['transferred_node_id'] == init_data[i][
                                        'nodeId']:
                                        from_cache[i2] += 1
                                    else:
                                        normal_count[i2] += 1
                            else:
                                for i3 in range(0, 24):
                                    if init_data[i]['records'][i1]['data']['transferred_node_id'] == init_data[i][
                                        'nodeId']:
                                        from_cache[i3] += 1
                                    else:
                                        normal_count[i3] += 1

                        else:
                            if init_data[i]['records'][i1]['data']['end_time'] < end_timeStamp:
                                k6 = panduan_shijianduan(init_data[i]['records'][i1]['data']['start_time'])
                                k7 = panduan_shijianduan(init_data[i]['records'][i1]['data']['end_time'])
                                for i4 in range(k6, k7 + 1):
                                    if init_data[i]['records'][i1]['data']['transferred_node_id'] == init_data[i][
                                        'nodeId']:
                                        from_cache[i4] += 1
                                    else:
                                        normal_count[i4] += 1
                            else:
                                k8 = panduan_shijianduan(init_data[i]['records'][i1]['data']['start_time'])
                                for i5 in range(k8, 24):
                                    if init_data[i]['records'][i1]['data']['transferred_node_id'] == init_data[i][
                                        'nodeId']:
                                        from_cache[i5] += 1
                                    else:
                                        normal_count[i5] += 1
for i6 in range(24):
    if super_count[i6] + normal_count[i6] + from_cache[i6] != 0:
        super_count_PR[i6] = super_count[i6] / (super_count[i6] + normal_count[i6] + from_cache[i6])
        normal_count_PR[i6] = normal_count[i6] / (super_count[i6] + normal_count[i6] + from_cache[i6])
        from_cache_PR[i6] = from_cache[i6] / (super_count[i6] + normal_count[i6] + from_cache[i6])
    else:
        super_count_PR[i6]=0
        normal_count_PR[i6]=0
        from_cache_PR[i6]=0
print(super_count_PR)
print(normal_count_PR)
print(from_cache_PR)
print(sum_1)
print(block_dict)
print(download_time)
print(min(download_time))

plt.figure(1)
ax = subplot(1, 1, 1)
xmajorLocator = MultipleLocator(1)
x = np.arange(24)
str4 = '%s%s%s%s' % (str11, '——', str12, '内，block下载情况')
plt.xticks(x, (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '   21:00', '   22:00', '   23:00'))
plt.title(str4)
plt.xlabel('时间/小时')
plt.ylabel('block数目/个')
plt.bar(x, height=super_count, color='red', label="From Super Node", bottom=normal_count)
plt.bar(x, height=normal_count, color='green', label="From User Node")
plt.legend()

plt.figure(2)
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
plt.bar(x, height=super_count, color='red', label="From Super Node", bottom=from_cache)
plt.bar(x, height=normal_count, color='green', label="From User Node")
plt.bar(x, height=from_cache, color='blue', label="From Cache", bottom=normal_count)
plt.legend()

plt.figure(3)  # 图3
len3 = len(block_dict)
ax = subplot(1, 1, 1)
xmajorLocator = MultipleLocator(1)
x = 1 + np.arange(len3)
y = block_dict.values()
str2 = '%s%s%s%s' % (str11, '——', str12, '内，每个节点的block下载情况')
plt.title(str2)
plt.xlabel('节点编号')
plt.ylabel('block数目/个')
plt.xticks(x)
plt.bar(x, y, color='blue')

# 图2
plt.figure(4)
ax = subplot(1, 1, 1)
# res = stats.relfreq(download_time, numbins=10)
# x = res.lowerlimit + np.linspace(0, res.binsize * res.frequency.size, res.frequency.size)
# y = np.cumsum(res.frequency)
plt.hist(download_time,100000,density=True, cumulative=True, histtype='step')
#plt.plot(x, y)
plt.title('数据块下载耗时的累积分布图')
plt.xlabel('download time/秒')
plt.ylabel('CDF')
plt.grid(True)  # 产生网格

plt.figure(5)
ax = subplot(2, 1, 1)
xmajorLocator = MultipleLocator(1)
x = np.arange(24)
str3 = '%s%s%s%s' % (str11, '——', str12, '内，P2P流量统计情况')
plt.plot(x, super_count_PR,color='red',label="From Super Node")
plt.plot(x, normal_count_PR,color='green',label="From User Node")
plt.plot(x, from_cache_PR,color='blue',label="From Cache")
plt.grid(True)  # 产生网格
plt.title(str3)
plt.legend()
plt.xlabel('时间/小时')
plt.ylabel('利用率')
plt.xticks(x, (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '   21:00', '   22:00', '   23:00'))
# plt.figure(5)
# ax = subplot(2, 1, 2)
# xmajorLocator = MultipleLocator(1)
# x = np.arange(24)
# bar_width = 0.3
# str3 = '%s%s%s%s' % (str11, '——', str12, '内，P2P流量统计情况')
# plt.bar(x-bar_width, super_count_PR, width=0.3, color='red', label="From Super Node")
# plt.bar(x+ bar_width , normal_count_PR, width=0.3, color='green', label="From User Node")
# plt.bar(x  , from_cache_PR, width=0.3, color='blue', label="From Cache")
# plt.grid(True)  # 产生网格
# plt.title(str3)
# plt.xlabel('时间/小时')
# plt.ylabel('概率')
# plt.xticks(x, (
#     '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
#     '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '   21:00', '   22:00', '   23:00'))
# plt.legend()
plt.show()
