# -*- coding: UTF-8 -*-
import numpy as np
# import demjson
import os
import json
import time
import matplotlib.pyplot as plt
import math
import string
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
download_time1 = [] #<=100
super_node_id = 'TVfZ-LQn7ZxenP8gsnky-F_J4WM'

start_time0 = '2019-04-30 00:00:00'
end_time0 = '2019-05-05 00:00:00'
timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
start_timeStamp = 1000 * int(time.mktime(timeArray1))
end_timeStamp = 1000 * int(time.mktime(timeArray2))

# 开始
file_path = "C://Users/dou/Desktop/1/zhuan"
files = os.listdir(file_path)
# print(files)
# len_list = len(files)
# for i in range(len_list):
str1 = "C://Users/dou/Desktop/1/zhuan/"
new_list_path = [str1 + x for x in files]  # list里存文件夹里所有文件的绝对路径
len_new_list_path = len(new_list_path)
for file_i in range(len_new_list_path):  # 文件循环
    file = open(new_list_path[file_i], 'r', encoding='gb18030', errors='ignore')
    for line1 in file.readlines():
        if line1.startswith('{"name":'):
            init_data.append(json.loads(line1))
len1 = len(init_data)
for i in range(len1):
    if init_data[i]['name'] == 'Download Record':
        # this_time_starttime.append([])
        len2 = len(init_data[i]['records'])
        for i1 in range(len2):  # 每条日志的所有block
            if init_data[i]['records'][i1]['data']['is_success'] is True:
                if init_data[i]['records'][i1]['data']['end_time'] >= start_timeStamp and \
                        init_data[i]['records'][i1]['data']['start_time'] <= end_timeStamp:
                    if init_data[i]['records'][i1]['data']['transferred_node_id'] == super_node_id:
                        download_time.append((init_data[i]['records'][i1]['data']['end_time']
                                              - init_data[i]['records'][i1]['data']['start_time']) / 1000)
                        if  (init_data[i]['records'][i1]['data']['end_time']
                                              - init_data[i]['records'][i1]['data']['start_time']) / 1000==298.821:
                           print(init_data[i])

# print(download_time)
# print(min(download_time))
# print(max(download_time))
for j in range(len(download_time)):
    if download_time[j]<=100:
        download_time1.append(download_time[j])
print(download_time1)

plt.figure(1)
ax = subplot(1, 1, 1)
# res = stats.relfreq(download_time, numbins=10)
# x = res.lowerlimit + np.linspace(0, res.binsize * res.frequency.size, res.frequency.size)
# y = np.cumsum(res.frequency)
plt.hist(download_time1,100000,density=True, cumulative=True, histtype='step')
#plt.plot(x, y)
plt.title('from user的数据块下载耗时的累积分布图')
plt.xlabel('download time/秒')
plt.ylabel('CDF')
plt.grid(True)  # 产生网格
plt.show()