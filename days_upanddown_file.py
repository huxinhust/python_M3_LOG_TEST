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
import csv

fig = plt.figure()
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 初始化
init_data = []
upanddown_dict = {}
file_down_up_file_num = {}
final_ = {}

start_time0 = '2019-04-30 00:00:00'
end_time0 = '2019-05-07 00:00:00'
days = 7
timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
start_timeStamp = 1000 * int(time.mktime(timeArray1))
end_timeStamp = 1000 * int(time.mktime(timeArray2))


def panduan_shijianduan(timestamp):
    time1 = (timestamp - start_timeStamp) / (3600000 * 24)
    kk = math.floor(time1)
    return kk


# 开始处理下载日志
file_path = "C://Users/dou/Desktop/1/true_data/zhuan"
files = os.listdir(file_path)
# print(files)
# len_list = len(files)
# for i in range(len_list):
str1 = "C://Users/dou/Desktop/1/true_data/zhuan/"
new_list_path = [str1 + x for x in files]  # list里存文件夹里所有文件的绝对路径
len_new_list_path = len(new_list_path)

for file_i in range(len_new_list_path):  # 文件循环
    file = open(new_list_path[file_i], 'r', encoding='gb18030', errors='ignore')
    for line1 in file.readlines():
        if line1.startswith('{"name":"Download Record'):
            init_data.append(json.loads(line1))
# print(init_data)
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

        if len(this_time_starttime[i]) != 0 and len(this_time_endtime[i]) != 0:
            file_starttime = min(this_time_starttime[i])
            file_endtime = max(this_time_endtime[i])
            if file_endtime >= start_timeStamp and file_starttime <= end_timeStamp:
                if init_data[i]['nodeId'] not in file_down_up_file_num:
                    file_down_up_file_num[init_data[i]['nodeId']] = [[], [], []]
                    for j1 in range(days):
                        file_down_up_file_num[init_data[i]['nodeId']][0].append(0)
                        file_down_up_file_num[init_data[i]['nodeId']][1].append(0)
                        file_down_up_file_num[init_data[i]['nodeId']][2].append(0)
            if file_starttime < start_timeStamp:
                if file_endtime < end_timeStamp:
                    k1 = panduan_shijianduan(file_endtime)
                    if init_data[i]['success'] is True:  # 下载成功
                        for i2 in range(0, k1 + 1):
                            file_down_up_file_num[init_data[i]['nodeId']][1][i2] += 1

                    else:  # 下载失败
                        for i3 in range(0, k1 + 1):
                            file_down_up_file_num[init_data[i]['nodeId']][2][i3] += 1
                else:
                    if init_data[i]['success'] is True:  # 下载成功
                        for i4 in range(days):
                            file_down_up_file_num[init_data[i]['nodeId']][1][i4] += 1
                    else:  # 下载失败
                        for i5 in range(days):
                            file_down_up_file_num[init_data[i]['nodeId']][2][i5] += 1
            else:
                if file_endtime < end_timeStamp:
                    k2 = panduan_shijianduan(file_starttime)
                    k3 = panduan_shijianduan(file_endtime)
                    if init_data[i]['success'] is True:  # 下载成功
                        for i6 in range(k2, k3 + 1):
                            file_down_up_file_num[init_data[i]['nodeId']][1][i6] += 1
                    else:
                        for i7 in range(k2, k3 + 1):
                            file_down_up_file_num[init_data[i]['nodeId']][2][i7] += 1
                else:

                    k4 = panduan_shijianduan(file_starttime)
                    if init_data[i]['success'] is True:  # 下载成功
                        for i8 in range(k4, days):
                            file_down_up_file_num[init_data[i]['nodeId']][1][i8] += 1
                    else:
                        for i9 in range(k4, days):
                            file_down_up_file_num[init_data[i]['nodeId']][1][i9] += 1
# print(file_down_up_file_num)
# 上传数据的处理
up_init_data = []
with open("E://科研/p2p/大规模测试/Untitled-1.csv", 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    fieldnames = next(reader)
    # print(fieldnames)
    csv_reader = csv.DictReader(f,
                                fieldnames=fieldnames)  # self._fieldnames = fieldnames   # list of keys for the dict 以list的形式存放键名
    for row in csv_reader:
        up_data = {}
        for k, v in row.items():

            up_data[k] = v
        up_init_data.append(up_data)
#print(up_init_data[0])#存上传日志的数据
len3 = len(up_init_data)
for j2 in range(len3):
    up_init_data[j2][' create_time'] = int(up_init_data[j2][' create_time'])
    if start_timeStamp <= up_init_data[j2][' create_time'] <= end_timeStamp:
        #print(up_init_data[j2][' owner_id'].strip())
        if up_init_data[j2][' owner_id'].strip() not in file_down_up_file_num:
            file_down_up_file_num[up_init_data[j2][' owner_id'].strip()] = [[], [], []]
            for j1 in range(days):
                file_down_up_file_num[up_init_data[j2][' owner_id'].strip()][0].append(0)
                file_down_up_file_num[up_init_data[j2][' owner_id'].strip()][1].append(0)
                file_down_up_file_num[up_init_data[j2][' owner_id'].strip()][2].append(0)

        k5 = panduan_shijianduan(up_init_data[j2][' create_time'])
        file_down_up_file_num[up_init_data[j2][' owner_id'].strip()][0][k5] += 1
# print(file_down_up_file_num)

# df1 = pd.DataFrame(file_down_up_file_num)
# str15 = 'm' + '.xlsx'
# df1.to_excel(str15, sheet_name='Data1', index=False)

for key1 in file_down_up_file_num:
    final_[key1] = []
    for j3 in range(days):
        final_[key1].append([])
        for j4 in range(3):
            final_[key1][j3].append(0)
    for j5 in range(days):
        final_[key1][j5][0] = file_down_up_file_num[key1][0][j5]
        final_[key1][j5][1] = file_down_up_file_num[key1][1][j5]
        final_[key1][j5][2] = file_down_up_file_num[key1][2][j5]
#print(final_)
df1 = pd.DataFrame(final_)
str15 = 'n' + '.xlsx'
df1.to_excel(str15, sheet_name='Data1', index=False)