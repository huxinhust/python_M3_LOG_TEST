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

init_data = []
Regist_unRegist_Time_dict = {}
lst_24 = []
table_dict = {}
new_dict = {}

lst_24_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst_24_single = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst_24_single2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
node_id_single = 'vtadlCs3NHmddm2Q4JiSuc8yEcI'
connect_num = {}
start_time0 = '2019-05-06 00:00:00'
end_time0 = '2019-05-07 00:00:00'
start_time0_single = '2019-05-06 00:00:00'
end_time0_single = '2019-05-07 00:00:00'
# 转为时间数组
timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray3 = time.strptime(start_time0_single, "%Y-%m-%d %H:%M:%S")  # 时间戳
timeArray4 = time.strptime(end_time0_single, "%Y-%m-%d %H:%M:%S")  # 时间戳
start_timeStamp = 1000 * int(time.mktime(timeArray1))
end_timeStamp = 1000 * int(time.mktime(timeArray2))
start_timeStamp_single = 1000 * int(time.mktime(timeArray3))
end_timeStamp_single = 1000 * int(time.mktime(timeArray4))
#print(start_timeStamp)
#print(end_timeStamp)
timestam11 = float(start_timeStamp / 1000)
timeArray11 = time.localtime(timestam11)
str11 = '%s%s%s%s%s%s%s%s' % (
    timeArray11.tm_year, '-', timeArray11.tm_mon, '-', timeArray11.tm_mday, '-', timeArray11.tm_hour, '点')
timestam12 = float(end_timeStamp / 1000)
timeArray12 = time.localtime(timestam12)
str12 = '%s%s%s%s%s%s%s%s' % (
    timeArray12.tm_year, '-', timeArray12.tm_mon, '-', timeArray12.tm_mday, '-', timeArray12.tm_hour, '点')
timestam13 = float(start_timeStamp_single / 1000)
timeArray13 = time.localtime(timestam13)
str13 = '%s%s%s%s%s%s%s%s' % (
    timeArray13.tm_year, '-', timeArray13.tm_mon, '-', timeArray13.tm_mday, '-', timeArray13.tm_hour, '点')
timestam14 = float(end_timeStamp_single / 1000)
timeArray14 = time.localtime(timestam14)
str14 = '%s%s%s%s%s%s%s%s' % (
    timeArray14.tm_year, '-', timeArray14.tm_mon, '-', timeArray14.tm_mday, '-', timeArray14.tm_hour, '点')
print(str11)


def panduan_shijianduan(timestamp):
    time1 = (timestamp - start_timeStamp) / 3600000
    kk = math.floor(time1)
    return kk


# 导入日志
fp = open("C://Users/dou/Desktop/1/true_data/naming-server-standalone-2019-05-09-1.log")
for line1 in fp.readlines():
    if line1.startswith('{"info'):
        init_data.append(json.loads(line1))
len1 = len(init_data)
for i in range(len1):
    if init_data[i]['info']['superNode'] is False:
        # print(init_data[i])
        # for key in init_data[i]:
        #     print(key)
        if init_data[i]['info']['nodeId'] not in table_dict:
            table_dict[init_data[i]['info']['nodeId']] = [init_data[i]['info']['name']]
        if init_data[i]['info']['nodeId'] not in Regist_unRegist_Time_dict:  # 如果nodeId在字典中未出现过
            Regist_unRegist_Time_dict[init_data[i]['info']['nodeId']] = [[init_data[i]['registTime'], 0]]  # 在字典中加入键值对
            if init_data[i]['unRegistTime'] is not None:
                Regist_unRegist_Time_dict[init_data[i]['info']['nodeId']][0][1] = init_data[i]['unRegistTime']
        else:  # 如果nodeId在字典中出现过(第一次上线还未离线 第x次上线..）
            len2 = len(Regist_unRegist_Time_dict[init_data[i]['info']['nodeId']])
            len3 = len2 - 1
            flag = 0
            for j in range(len2):
                if Regist_unRegist_Time_dict[init_data[i]['info']['nodeId']][j][0] == init_data[i]['registTime']:
                    flag = flag + 1
            if flag != 0 and init_data[i]['unRegistTime'] is not None:
                Regist_unRegist_Time_dict[init_data[i]['info']['nodeId']][j][1] = init_data[i]['unRegistTime']
            if flag == 0:
                Regist_unRegist_Time_dict[init_data[i]['info']['nodeId']].append([init_data[i]['registTime'], 0])
# print(Regist_unRegist_Time_dict)
for key_i in Regist_unRegist_Time_dict:  # 图1
    len2 = len(Regist_unRegist_Time_dict[key_i])
    arr = []  # 存括号
    arr1 = []  #
    for j in range(len2):
        if len(arr) == 0:
            new_dict[key_i] = []
            arr.append('{')
            if Regist_unRegist_Time_dict[key_i][j][1] != 0:
                arr.append('}')
                new_dict[key_i].append([Regist_unRegist_Time_dict[key_i][j][0], Regist_unRegist_Time_dict[key_i][j][1]])
            else:
                arr1.append(Regist_unRegist_Time_dict[key_i][j][0])
        else:
            if arr.pop(-1) != '{':
                arr.append('{')
                if Regist_unRegist_Time_dict[key_i][j][1] != 0:
                    arr.append('}')
                    new_dict[key_i].append(
                        [Regist_unRegist_Time_dict[key_i][j][0], Regist_unRegist_Time_dict[key_i][j][1]])
                else:
                    arr1.append(Regist_unRegist_Time_dict[key_i][j][0])
            else:
                if Regist_unRegist_Time_dict[key_i][j][1] != 0:
                    arr.append('}')
                    new_dict[key_i].append([arr1.pop(-1), Regist_unRegist_Time_dict[key_i][j][1]])

    if len(arr) != 0 and arr.pop(-1) == '{':
        new_dict[key_i].append([arr1.pop(-1), 0])

# print(new_dict)
len5 = len(new_dict)
total = []
for iii in range(len5):
    total.append(0)
total_connect_num = []
for iiii in range(len5):
    total_connect_num.append(0)
num_i = 0
for keyii in new_dict:
    num_i = num_i + 1
    for jj in range(len(new_dict[keyii])):
        if new_dict[keyii][jj][1] >= start_timeStamp and new_dict[keyii][jj][0] <= end_timeStamp:
            if new_dict[keyii][jj][1] != 0:
                if new_dict[keyii][jj][0] <= start_timeStamp:
                    if start_timeStamp < new_dict[keyii][jj][1] < end_timeStamp:
                        total[num_i - 1] = total[num_i - 1] + new_dict[keyii][jj][1] - start_timeStamp
                        total_connect_num[num_i - 1] = total_connect_num[num_i - 1] + 1
                    if new_dict[keyii][jj][1] > end_timeStamp:
                        total[num_i - 1] = total[num_i - 1] + end_timeStamp - start_timeStamp
                        total_connect_num[num_i - 1] = total_connect_num[num_i - 1] + 1
                else:
                    if new_dict[keyii][jj][1] < end_timeStamp:
                        total[num_i - 1] = total[num_i - 1] + new_dict[keyii][jj][1] - new_dict[keyii][jj][0]
                        total_connect_num[num_i - 1] = total_connect_num[num_i - 1] + 1
                    else:
                        total[num_i - 1] = total[num_i - 1] + end_timeStamp - new_dict[keyii][jj][0]
                        total_connect_num[num_i - 1] = total_connect_num[num_i - 1] + 1
            else:
                if new_dict[keyii][jj][0] <= start_timeStamp:
                    total[num_i - 1] = total[num_i - 1] + end_timeStamp - start_timeStamp
                    total_connect_num[num_i - 1] = total_connect_num[num_i - 1] + 1
                else:
                    total[num_i - 1] = total[num_i - 1] + end_timeStamp - new_dict[keyii][jj][0]
                    total_connect_num[num_i - 1] = total_connect_num[num_i - 1] + 1
lst_key = list(table_dict.keys())
for mm in range(len(total)):
    total[mm] = total[mm] / 3600000
    table_dict[lst_key[mm]].append(total[mm])
    table_dict[lst_key[mm]].append(total_connect_num[mm])
# print(type(table_dict[lst_key[mm]]))
# total.sort(reverse=True)
# print(lst_key)
# print(total)
# print(table_dict)
# print(total_connect_num)
lst1=[]
for key1 in table_dict:
    if table_dict[key1][1] == 0 and table_dict[key1][2] == 0:
        lst1.append(key1)
#print(table_dict)
#print(lst1)
for key2 in lst1:
    del table_dict[key2]
#print(table_dict)
df1=pd.DataFrame(table_dict)
str15=str11+'.xlsx'
df1.to_excel(str15,sheet_name='Data1',index=False)
#print(df1)
len4 = len(new_dict)
for i in range(len4):
    lst_24.append([])
    for j in range(24):
        lst_24[i].append(0)
num_key_i = 0
for key_i in new_dict:  # 图1
    num_key_i = num_key_i + 1
    len2 = len(new_dict[key_i])
    for j in range(len2):
        if new_dict[key_i][j][1] == 0:
            if new_dict[key_i][j][0] < start_timeStamp:
                for k5 in range(0, 24):
                    lst_24[num_key_i - 1][k5] = 1
            if start_timeStamp < new_dict[key_i][j][0] < end_timeStamp:
                k = panduan_shijianduan(new_dict[key_i][j][0])
                for k6 in range(k, 24):
                    lst_24[num_key_i - 1][k6] = 1

        if new_dict[key_i][j][1] != 0:
            if new_dict[key_i][j][0] <= end_timeStamp and new_dict[key_i][j][
                1] >= start_timeStamp:
                # print(Regist_unRegist_Time_dict[key_i][j])
                if new_dict[key_i][j][0] <= start_timeStamp:
                    if new_dict[key_i][j][1] < end_timeStamp:
                        k = panduan_shijianduan(new_dict[key_i][j][1])
                        # print(k)
                        for k1 in range(0, k + 1):
                            lst_24[num_key_i - 1][k1] = 1
                    else:
                        for k2 in range(24):
                            lst_24[num_key_i - 1][k2] = 1
                else:
                    k = panduan_shijianduan(new_dict[key_i][j][0])
                    if new_dict[key_i][j][1] < end_timeStamp:
                        m = panduan_shijianduan(new_dict[key_i][j][1])
                        for k3 in range(k, m + 1):
                            lst_24[num_key_i - 1][k3] = 1
                    else:
                        for k4 in range(k, 24):
                            lst_24[num_key_i - 1][k4] = 1
# print(lst_24)

for jk in range(24):
    for mk in range(len4):
        lst_24_1[jk] = lst_24[mk][jk] + lst_24_1[jk]
print(lst_24_1)
# 第二张图
len3 = len(new_dict[node_id_single])
for n in range(len3):
    if new_dict[node_id_single][n][1] == 0:
        if new_dict[node_id_single][n][0] < start_timeStamp_single:
            for k6 in range(24):
                lst_24_single[k6] = lst_24_single[k6] + 1
        if start_timeStamp_single < new_dict[node_id_single][n][0] < end_timeStamp_single:
            k = panduan_shijianduan(new_dict[node_id_single][n][0])
            for k4 in range(k, 24):
                lst_24_single[k4] = lst_24_single[k4] + 1

    if new_dict[node_id_single][n][1] != 0:
        if new_dict[node_id_single][n][0] <= end_timeStamp_single and \
                new_dict[node_id_single][n][1] >= start_timeStamp_single:
            if new_dict[node_id_single][n][0] <= start_timeStamp_single:
                if new_dict[node_id_single][n][1] < end_timeStamp_single:
                    k = panduan_shijianduan(new_dict[node_id_single][n][1])
                    # print(k)
                    for k5 in range(0, k + 1):
                        lst_24_single[k5] = lst_24_single[k5] + 1
                else:
                    for k6 in range(24):
                        lst_24_single[k6] = lst_24_single[k6] + 1
            else:
                k = panduan_shijianduan(new_dict[node_id_single][n][0])
                if new_dict[node_id_single][n][1] < end_timeStamp_single:
                    m = panduan_shijianduan(new_dict[node_id_single][n][1])
                    for k3 in range(k, m + 1):
                        lst_24_single[k3] = lst_24_single[k3] + 1
                else:
                    for k4 in range(k, 24):
                        lst_24_single[k4] = lst_24_single[k4] + 1
# print(lst_24_single)
for ii in range(24):
    if lst_24_single[ii] != 0:
        lst_24_single2[ii] = 1
# print(lst_24_single2)
# print(table_dict)
# print(len(table_dict))
# print(len(total))
# print(len(lst_key))


plt.figure(1)
ax = subplot(2, 1, 1)
xmajorLocator = MultipleLocator(1)
x = np.arange(24)
y = lst_24_1
ax.xaxis.set_major_locator(xmajorLocator)
str = '%s%s%s%s' % (str11, '——', str12, '内，节点活跃情况')

# plt.xticks(x, ('0-1点', '1-2点', '2-3点', '3-4点', '4-5点', '5-6点', '6-7点', '7-8点','8-9点','9-10点','10-11点','11-12点','12-13点','13-14点','14-15点','15-16点','16-17点','17-18点','18-19点','19-20点','20-21点','21-22点','22-23点','23-24点'))
plt.xticks(x, (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '   21:00', '   22:00', '   23:00'))
plt.title(str)
plt.xlabel('时间/小时')
plt.ylabel('在线节点数目/个')
plt.bar(x, y, color='blue')

plt.figure(1)
ax = subplot(2, 1, 2)
xmajorLocator = MultipleLocator(1)
x = np.arange(24)
y = lst_24_single2
ax.xaxis.set_major_locator(xmajorLocator)
str1 = '%s%s%s%s%s%s' % (str13, '——', str14, '内，节点', node_id_single, '的活跃情况(ipv4)')
plt.xticks(x, (
    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '     21:00', '    22:00', '    23:00'))
plt.title(str1)
plt.xlabel('时间/小时')
plt.ylabel('活跃情况')
# plt.bar(x, y, color='blue',width =1)
plt.plot(x, y, marker='o', color='blue')
plt.show()
