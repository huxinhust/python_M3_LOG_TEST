# -*- coding: UTF-8 -*-
# 图6
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
file_name_point = 'OK_Chuyển động vật lý hoàn hảo_Part 01.mp4'
success_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fail_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
file_download_time = {}
file_start_end_time = {}
start_time0 = '2019-05-03 00:00:00'
end_time0 = '2019-05-04 00:00:00'
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
fp = open("C://Users/dou/Desktop/1/benchmark-server-standalone1-2019-05-03-1.log", encoding="UTF-8")
for line1 in fp.readlines():
    if line1.startswith('{"name":'):
        init_data.append(json.loads(line1))
len1 = len(init_data)
this_time_starttime = []
for m2 in range(len1):
    this_time_starttime.append([])  # this_time_starttime=[[], []...... [], [], []]
this_time_endtime = []
for m1 in range(len1):
    this_time_endtime.append([])  # this_time_endtime=[[], []...... [], [], []]
sum_1 = 0
for i in range(len1):
    if init_data[i]['name'] == 'Download Record':
        # this_time_starttime.append([])
        len2 = len(init_data[i]['records'])
        for i1 in range(len2):  # 每条日志的所有block
            if len(init_data[i]['records']) != 0:
                if init_data[i]['records'][i1]['data']['is_success'] is True:
                    if init_data[i]['records'][i1]['data']['end_time'] >= start_timeStamp and \
                            init_data[i]['records'][i1]['data']['start_time'] <= end_timeStamp:
                        this_time_starttime[i].append(init_data[i]['records'][i1]['data']['start_time'])
                        this_time_endtime[i].append(init_data[i]['records'][i1]['data']['end_time'])

        if len(this_time_starttime[i]) != 0 and len(this_time_endtime[i]) != 0:
            file_starttime = min(this_time_starttime[i])
            file_endtime = max(this_time_endtime[i])
            if init_data[i]['properties']['name'] not in file_start_end_time:
                file_start_end_time[init_data[i]['properties']['name']] = [[file_starttime, file_endtime]]
            else:
                file_start_end_time[init_data[i]['properties']['name']].append([file_starttime, file_endtime])
            # print(file_start_end_time)
            if init_data[i]['success'] is True:
                # 判断时间段
                if file_starttime < start_timeStamp:
                    if file_endtime < end_timeStamp:
                        k1 = panduan_shijianduan(file_endtime)
                        for i2 in range(0, k1 + 1):
                            success_count[i2] += 1
                    else:
                        for i3 in range(0, 24):
                            success_count[i3] += 1
                else:
                    if file_endtime < end_timeStamp:
                        k2 = panduan_shijianduan(file_starttime)
                        k3 = panduan_shijianduan(file_endtime)
                        for i4 in range(k2, k3 + 1):
                            success_count[i4] += 1
                    else:
                        k4 = panduan_shijianduan(file_starttime)
                        for i5 in range(k4, 24):
                            success_count[i5] += 1
            else:
                if file_endtime >= start_timeStamp and \
                        file_starttime <= end_timeStamp:
                    # 判断时间段
                    if file_starttime < start_timeStamp:
                        if file_endtime < end_timeStamp:
                            k1 = panduan_shijianduan(file_endtime)
                            for i2 in range(0, k1 + 1):
                                fail_count[i2] += 1
                        else:
                            for i3 in range(0, 24):
                                fail_count[i3] += 1
                    else:
                        if file_endtime < end_timeStamp:
                            k2 = panduan_shijianduan(file_starttime)
                            k3 = panduan_shijianduan(file_endtime)
                            for i4 in range(k2, k3 + 1):
                                fail_count[i4] += 1
                        else:
                            k4 = panduan_shijianduan(file_starttime)
                            for i5 in range(k4, 24):
                                fail_count[i5] += 1
print(success_count)
print(fail_count)
#print(file_start_end_time)
for key in file_start_end_time:
    len3 = len(file_start_end_time[key])
    for i2 in range(len3):
        if key not in file_download_time:
            time1 = (file_start_end_time[key][i2][1] - file_start_end_time[key][i2][0]) / 1000
            file_download_time[key] = [time1]
        else:
            time2 = (file_start_end_time[key][i2][1] - file_start_end_time[key][i2][0]) / 1000
            file_download_time[key].append(time2)
print(file_download_time)

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

# plt.figure(2)  # 图5
# ax = subplot(1, 1, 1)
# xmajorLocator = MultipleLocator(1)
# x = 1 + np.arange(len(file_download_time[file_name_point]))
# y=file_download_time[file_name_point]
# str2 = '%s%s%s%s%s%s' % (str11, '——', str12, '内，',file_name_point,'文件的下载时间分布')
# plt.title(str2)
# plt.xlabel('下载次数')
# plt.ylabel('下载时间')
# plt.bar(x,height= y, color='blue')
# plt.xticks(x)
plt.show()
