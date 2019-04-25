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
str2 = 'ConnectTime Test'
data_list = []  # 存放wanted日志对象
for line in fp.readlines():
    if str2 in line :
        if line.startswith('{"name"'):
            data_list.append(line)
        # print(line)
# print(data_list)
# print(len(data_list))

# 初始化
connect_Time_save1 = []
connect_Time_save2 = []
for m1 in range(100):  # 设有100个日志对象（100次测试）
    connect_Time_save1.append([])  # latency_save=[[], []...... [], [], []]
for m2 in range(100):  # 设有100个日志对象（100次测试）
    connect_Time_save2.append([])  # latency_save=[[], []...... [], [], []]
    y1 = []
    for m3 in range(100):  # 设有100个日志对象（100次测试）
        y1.append([])  # latency_save=[[], []...... [], [], []]
    y2 = []
    for m4 in range(100):  # 设有100个日志对象（100次测试）
        y2.append([])  # latency_save=[[], []...... [], [], []]
init_data = []
src_node = []
des_node = []
connect_test_save = []

# 开始日志分析
for i in range(len(data_list)):  # 循环所有日志对象
    # print(data_list[0])
    init_data.append(json.loads(data_list[i]))  # init_data,列表，存放wanted日志对象（json格式）
    if init_data[i]['name'] == 'ConnectTime Test':
        if init_data[i]['success'] is True:
            if init_data[i]['records'] != []:
                src_node.append((init_data[i]['properties'])['srcName'])
                des_node.append((init_data[i]['properties'])['desName'])
                # print(init_data[i])
                connect_test_save.append(init_data[i])
                len1 = len(connect_test_save)
                len2 = len1 - 1
                for k in range(0, 3):
                    connect_Time_save1[len2].append((init_data[i]['records'][k])['data']['testResult'])
                    connect_Time_save2[len2].append((init_data[i]['records'][k])['data']['connectTime'])
# print(connect_test_save)
print(connect_Time_save1)
print(connect_Time_save2)

figure_num = connect_Time_save2.index([])
for num in range(figure_num):
    # print(num)
    num1=num+1
    plt.figure(num1)
    str2 = 'P2P第' + str(num1) + '次测试(' + str(src_node[num]) + '-' + str(des_node[num]) + ')—连接时长情况'
    ax = subplot(1, 1, 1)
    xmajorLocator = MultipleLocator(1)
    x = np.linspace(0, len(connect_Time_save2[num]), len(connect_Time_save2[num]))  # 定义x轴从0到，并且定义个样品点
    y=connect_Time_save2[num]
    # for num1 in range(0, 3):
    #     if connect_Time_save2[num][num1] >= 10000:
    #         y1[num].append(connect_Time_save2[num][num1])
    #     else:
    #         y2[num].append(connect_Time_save2[num][num1])
    # print(y1)
    # print(y2)
    ax.xaxis.set_major_locator(xmajorLocator)
    plt.hlines(10000, 0, 3, colors="r", linestyles="dashed",label="连接时长为10000ms")
    plt.title(str2)
    plt.xlabel('传输模式')
    plt.ylabel('时间/ms')
    plt.plot(x, y, marker='o', color='blue')
    #plt.scatter(x, y, marker='o', color='blue')
    # plt.(scatterx, y1, marker='x', color='g', label='1', s=30)
    # plt.scatter(x, y2, marker='+', color='r', label='2', s=30)
    # plt.legend(loc='upper right')
    plt.legend(loc=0, ncol=1)
    plt.xticks(x, ('BothTransfer', 'SingleTransfer', 'NullTransfer'))
    plt.show()
