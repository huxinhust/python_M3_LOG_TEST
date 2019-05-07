# -*- coding: UTF-8 -*-
import numpy as np
# import demjson
import os
import json
import time
import matplotlib.pyplot as plt
import math
import seaborn as sns
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy import stats
import pandas as pd
import numpy as np

fig = plt.figure()
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

# 初始化
init_data = []

start_time0 = '2019-04-30 00:00:00'
end_time0 = '2019-05-04 23:59:59'
timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
start_timeStamp = 1000 * int(time.mktime(timeArray1))
end_timeStamp = 1000 * int(time.mktime(timeArray2))
bin1 = 4 * 60 * 60 * 1000
total_point = math.ceil((end_timeStamp - start_timeStamp) / bin1)
success_count = []
for j1 in range(total_point):
    success_count.append(0)
fail_count = []
for j2 in range(total_point):
    fail_count.append(0)


def panduan_shijianduan(timestamp):
    time1 = (timestamp - start_timeStamp) / (4 * 3600000)
    kk = math.floor(time1)
    return kk


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
this_time_starttime = []
for m2 in range(len1):
    this_time_starttime.append([])  # this_time_starttime=[[], []...... [], [], []]
this_time_endtime = []
for m1 in range(len1):
    this_time_endtime.append([])  # this_time_endtime=[[], []...... [], [], []]
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
    # print(this_time_endtime)
    # print(this_time_starttime)
    if len(this_time_starttime[i]) != 0 and len(this_time_endtime[i]) != 0:
        file_starttime = min(this_time_starttime[i])
        file_endtime = max(this_time_endtime[i])
        if init_data[i]['success'] is True:
            # 判断时间段
            if file_starttime < start_timeStamp:
                if file_endtime < end_timeStamp:
                    k1 = panduan_shijianduan(file_endtime)
                    for i2 in range(0, k1 + 1):
                        success_count[i2] += 1
                else:
                    for i3 in range(0, len1):
                        success_count[i3] += 1
            else:
                if file_endtime < end_timeStamp:
                    k2 = panduan_shijianduan(file_starttime)
                    k3 = panduan_shijianduan(file_endtime)
                    for i4 in range(k2, k3 + 1):
                        success_count[i4] += 1
                else:
                    k4 = panduan_shijianduan(file_starttime)
                    for i5 in range(k4, len1):
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
                        for i3 in range(0, len1):
                            fail_count[i3] += 1
                else:
                    if file_endtime < end_timeStamp:
                        k2 = panduan_shijianduan(file_starttime)
                        k3 = panduan_shijianduan(file_endtime)
                        for i4 in range(k2, k3 + 1):
                            fail_count[i4] += 1
                    else:
                        k4 = panduan_shijianduan(file_starttime)
                        for i5 in range(k4, len1):
                            fail_count[i5] += 1
print(success_count)
print(fail_count)
print(total_point)
plt.figure(1)  #
#time_range = pd.date_range('2019-04-30 00:00:00', periods=5, freq='4h')
ax = subplot(1, 1, 1)
xmajorLocator = MultipleLocator(1)
x = np.arange(total_point)
# str2 = '%s%s%s%s' % (str11, '——', str12, '内，文件下载情况')
plt.title('4.30--5.4日,文件下载情况(4小时间隔)')
plt.xlabel('时间')
plt.ylabel('次数')
plt.bar(x, height=success_count, color='green', label="文件下载成功次数")
plt.bar(x, height=fail_count, color='red', label="文件下载失败次数", bottom=success_count)

dti=pd.date_range(start='2019-04-30 00:00',end='2019-05-05 00:00', freq='4H')
pydate_array = dti.to_pydatetime()
date_only_array = np.vectorize(lambda s: s.strftime('%Y-%m-%d  %H:%M'))(pydate_array )
date_only_series = pd.Series(date_only_array)
xck=list(date_only_series)
print(xck)
plt.xticks(x-1.5,xck,rotation=45)
plt.legend()
plt.show()
