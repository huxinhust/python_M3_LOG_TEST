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

# 导入日志
fp = open("C://Users/dou/Desktop/benchmark-server-standalone1.log")
str3 = 'BandWidth Test'
data_list = []  # 存放wanted日志对象
for line in fp.readlines():
    if str3 in line:
        if line.startswith('{"name"'):
            data_list.append(line)
BandWidth_save = []
for m0 in range(100):  # 设有100个日志对象（100次测试）
    BandWidth_save.append([])  # latency_save=[[], []...... [], [], []]
init_data = []
src_node = []
des_node = []
BandWidth_test_save = []
# 开始日志分析
for i in range(len(data_list)):  # 循环所有日志对象
    # print(data_list[0])
    init_data.append(json.loads(data_list[i]))  # init_data,列表，存放wanted日志对象（json格式）
    if init_data[i]['name'] == 'BandWidth Test':
        if init_data[i]['success'] is True:
            if init_data[i]['records'] != []:

                src_node.append((init_data[i]['properties'])['srcName'])
                des_node.append((init_data[i]['properties'])['desName'])
                # print(init_data[i])
                BandWidth_test_save.append(init_data[i])
                len1 = len(BandWidth_test_save)
                len2 = len1 - 1
                for k in range(0,8):
                    print((init_data[i]['records'][k])['data']['outSpeed'])
                    BandWidth_save[len2].append((init_data[i]['records'][k])['data']['outSpeed'])
print(BandWidth_test_save)

figure_num = BandWidth_save.index([])
for num in range(figure_num):
    print(num)
    num1 = num + 1
    plt.figure(num1)
    str2 = 'P2P第' + str(num1) + '次测试(' + str(src_node[num]) + '-' + str(des_node[num]) + ')—带宽情况'
    ax = subplot(1, 1, 1)
    xmajorLocator = MultipleLocator(1)
    # x = np.linspace(0, len(BandWidth_save[num]), len(BandWidth_save[num]))  # 定义x轴从0到，并且定义个样品点
    x = np.arange(len(BandWidth_save[num]))
    y0 = BandWidth_save[num]
    y = [i * 8 / 1048576 for i in y0]
    print(x)
    print(y)
    # for num1 in range(0, 3):
    #     if connect_Time_save2[num][num1] >= 10000:
    #         y1[num].append(connect_Time_save2[num][num1])
    #     else:
    #         y2[num].append(connect_Time_save2[num][num1])
    # print(y1)
    # print(y2)
    ax.xaxis.set_major_locator(xmajorLocator)
    plt.title(str2)
    plt.xlabel('数据包大小/KB')
    plt.ylabel('传输速度/Mb/s')
    # plt.plot(x, y, marker='o', color='blue')
    plt.bar(x, y, color='blue')
    # plt.scatter(x, y, marker='o', color='blue')
    # plt.(scatterx, y1, marker='x', color='g', label='1', s=30)
    # plt.scatter(x, y2, marker='+', color='r', label='2', s=30)
    # plt.legend(loc='upper right')
    # plt.legend(loc=0, ncol=1)
    # for rect in y:
    #     rect=int(rect)
    #     height = rect.get_height()
    #     plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
    plt.xticks(x, ('2048', '4096', '8192', '16384', '32208','65536','131072','262144'))
    plt.show()
