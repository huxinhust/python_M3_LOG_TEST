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

fig = plt.figure()
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 导入日志
fp = open("C://Users/dou/Desktop/3benchmark-server-stan   dalone.log")
str1 = 'Ping Test'
str2 = 'ConnectTime Test'
data_list = []  # 存放wanted日志对象
for line in fp.readlines():
    if str1 in line:
        if line.startswith('{"name"'):
            data_list.append(line)
        # print(line)
# print(data_list)
# print(len(data_list))
# 初始化
latency_save = []
for m0 in range(100):  # 设有100个日志对象（100次测试）
    latency_save.append([])  # latency_save=[[], []...... [], [], []]
throughTime_save = []
jitterMax_save = []
for m2 in range(100):  # 设有100个日志对象（100次测试）
    jitterMax_save.append([])  # latency_save=[[], []...... [], [], []]
jitterMin_save = []
for m3 in range(100):  # 设有100个日志对象（100次测试）
    jitterMin_save.append([])  # latency_save=[[], []...... [], [], []]
connect_Time_save1 = []
connect_Time_save2 = []
for m4 in range(100):  # 设有100个日志对象（100次测试）
    connect_Time_save1.append([])  # latency_save=[[], []...... [], [], []]
for m5 in range(100):  # 设有100个日志对象（100次测试）
    connect_Time_save2.append([])  # latency_save=[[], []...... [], [], []]
init_data = []
src_node = []
des_node = []
ping_test_save = []
connect_test_save = []
# 开始日志分析
for i in range(len(data_list)):  # 循环所有日志对象
    # print(data_list[0])
    init_data.append(json.loads(data_list[i]))  # init_data,列表，存放wanted日志对象（json格式）
    # print(init_data[i])
    if init_data[i]['name'] == 'Ping Test':
        if init_data[i]['success'] is True:
            if init_data[i]['records'] != []:
                print(init_data[i])
                ping_test_save.append(init_data[i])
                len1 = len(ping_test_save)
                len2 = len1 - 1
                throughTime_save.append((init_data[i]['properties'])['throughTime'])
                src_node.append((init_data[i]['properties'])['srcName'])
                des_node.append((init_data[i]['properties'])['desName'])
                for j in range(0, 5):
                    latency_save[len2].append((init_data[i]['records'][j])['data']['latency'])
                    jitterMax_save[len2].append((init_data[i]['records'][j])['data']['jitterMax'])
                    jitterMin_save[len2].append((init_data[i]['records'][j])['data']['jitterMin'])
# print(latency_save)
# print(jitterMax_save)
# print(jitterMin_save)
# print(connect_Time_save1)
# print(connect_Time_save2)

# print(throughTime_save)

# NAT穿越时间绘图（all）
plt.figure(1)
ax = subplot(1, 1, 1)
xmajorLocator = MultipleLocator(1)
x = np.linspace(0, len(throughTime_save), len(throughTime_save))  # 定义x轴从0到，并且定义个样品点
y = throughTime_save
ax.xaxis.set_major_locator(xmajorLocator)
plt.title('throughTime')
plt.xlabel('测试次数/次')
plt.ylabel('NAT穿越时间/ms')
plt.plot(x, y, marker='o', color='blue')

# 时延、抖动绘图
figure_num = latency_save.index([])
for num in range(figure_num):
    # print(num)
    plt.figure(num + 2)
    ax = subplot(1, 1, 1)
    xmajorLocator = MultipleLocator(2)
    num1 = num + 1
    str2 = 'P2P第' + str(num1) + '次测试(' + str(src_node[num]) + '-' + str(des_node[num]) + ')—时延、抖动情况'
    plt.title(str2)
    plt.xlabel('数据包大小/Byte')
    plt.ylabel('时间/ms')
    x = np.arange(5)
    # x=[128,256,512,1024,2048]
    # x = [128,256,512,1024,2048]
    y1 = latency_save[num]
    y2 = jitterMin_save[num]
    y3 = jitterMax_save[num]
    ax.xaxis.set_major_locator(xmajorLocator)
    bar_width = 0.3
    # x1 = [i + bar_width for i in x]
    # x2 = [i + 2*bar_width for i in x]
    # print(x)
    # print(y1)
    # print(y2)
    # print(y3)
    plt.bar(x, y1, width=0.3, color='green', label="latency")
    plt.bar(x + bar_width, y3, width=0.3, color='red', label="jitterMax")
    plt.bar(x + bar_width * 2, y2, width=0.3, color='blue', label="jitterMin")
    plt.legend(loc=0, ncol=1)
    plt.xticks(x + bar_width, ('128', '256', '512', '1024', '2048'))
    plt.show()
