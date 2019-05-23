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
import string
import xlrd
import xlwt
from xlwt import *


#  将数据写入新文件

def data_write(file_path, datas):
    # print(datas)
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    # 将数据写入第 i 行，第 j 列
    for j in range(len(datas)):
        sheet1.write(j, 0, datas[j])

    f.save(file_path)  # 保存文件


fileName = "E://科研/p2p/大规模测试/真实数据的日志测试报告/test1.xlsx"
workbook = xlrd.open_workbook(fileName)
Data_sheet = workbook.sheets()[0]  # 通过索引获取
rowNum = Data_sheet.nrows  # sheet行数
colNum = Data_sheet.ncols  # sheet列数
cols = Data_sheet.col_values(0)
# print (cols)#存MID

userid_email_dist = {}
lst1 = []
lst2 = []
# 读取代码
fr = open("E://科研/p2p/大规模测试/MID_USERID.txt", 'r')
MID_USERID_dic = {}  # MID是key,USERID是value
keys = []  # 用来存储读取的顺序
for line in fr:
    v = line.strip().split(',')
    MID_USERID_dic[v[0]] = v[1]
    keys.append(v[0])
fr.close()
# print(MID_USERID_dic)

email_lst = ['709321440@qq.com', 'test1@qq.com', 'test@qq.com', 'ceshi@163.com', 'Support@antube.io',
             'kimkm1318@gmail.com',
             'nacomtech@gmail.com', 'techsimpleplus@gmail.com', 'starfishcluster@gmail.com', 'ufukyanhesap@gmail.com',
             'maryoriski44@gmail.com',
             'sunilpathak0308@gmail.com', 'saracie88@gmail.com', 'deparid123@gmail.com', 'capapwan23@yahoo.co.in',
             'aly452277@gmail.com',
             'hwadong154@gmail.com', 'fatihozogut8@gmail.com', 'd3de91_11@yahoo.com', 'jack452277@gmail.com',
             'nongvantuan6561@gmail.com',
             'hemayetuddin2277@gmail.com', 'amtodigitalstudio@gmail.com', 'agung_acer@hotmail.com',
             'noercah2@gmail.com', 'andri.crypto.currency@gmail.com',
             'mcfull79@gmail.com', 'melee039@gmail.com', 'mr4lte01@gmail.com', 'asyamsi@gmail.com',
             'sudiptadakshit1989@gmail.com', 'blu3summ3rs@gmail.com',
             'oguzarapasiatkinson@gmail.com', 'yilmazyarici@gmail.com', 'kokmeto@gmail.com', 'h31n4.1@gmail.com',
             'bsbrabia@gmail.com',
             'radiulislam1214@gmail.com', 'vs.dewangan17@gmail.com', 'anjanahogayamaradil@gmail.com',
             'bkaribandi8@gmail.com', 'nuril.always09@gmail.com',
             'nazir.khan2005@gmail.com', 'buzzultimate0@gmail.com', 'ranawat1987@gmail.com', 'ysh0984@gmail.com',
             'towfiqraj@gmail.com',
             'ruhanbd44@gmail.com', 'mxmahin786@gmail.com', 'enongdeka@gmail.com', 'tohaahmad72@gmail.com',
             'biroj007@gmail.com',
             'thuyhang1082015@gmail.com', 'jogilaguna@gmail.com', 'rajeshkumar51260@gmail.com', 'stoe901@gmail.com',
             'prastya.silvertis@gmail.com',
             'supunnishara@gmail.com', 'anayetahr@gmail.com', 'viatoromatic890@gmail.com', 'hasan.khagga123@gmail.com',
             'ekrem71@hotmail.com',
             'rafifakansa@gmail.com', 'siskapermata87@gmail.com', 'bestforex212@gmail.com', 'joshcarnice@gmail.com',
             'trunghoai199533@gmail.com',
             'ryanbonghanoy@gmail.com', 'jitencrackit2@gmail.com', 'nonengxx98@gmail.com', 'bubuzzultimate0@gmail.com',
             'gadingmarvel@gmail.com',
             'jayant.ibrampurkar@gmail.com', 'mysp2508@gmail.com', 'mrf100398@gmail.com', 'jaydjd611@gmail.com',
             '904455263@qq.com', 'badrulsyakir00@gmail.com',
             'tbnhon@gmail.com', 'daviddavid78154@gmail.com', 'juvieruel14@gmail.com', 'tuananh3987@gmail.com',
             'wdcho82@gamil.com', 'thanhtungvo7780@gmail.com',
             'wdcho82@gmail.com', 'fadelasrianto1995@gmail.com', 'raozeeshan73@gmail.com', 'yjoh8585@gmail.com',
             'jongpopo99@gmail.com', 'endar.fernandes@gmail.com',
             'WhiteR4bbitt@gmail.com', 'praxantpacific33@gmail.com', 'jj4375@gmail.com', 'rcxcof6@gmail.com',
             'jorjorann@gmail.com', 'leumpayy@gmail.com',
             'subashchandthakur0@gmail.com', 'niknev3386@gmail.com', 'ahr01934@gmail.com']
userid_lst = ['71eacd4a65ba4df387a0f11498bd30b1', '344bd7b38f444927a3ea4bf0b99c7b53',
              '9f3ccdc6cd914538872ae1fb815e68f3', '9fe0c2b214c54cb6901a26d3439fa330',
              '9a66674f875c4fbb9846b29e58915430', '57506d51304a4049ad95b45e21346074',
              '0deee0fb60a24c9b9fc80b5101823dee', 'ab2cc22aa01f40c08210becd0b856c42',
              '739f0c3b941c4949bd0361c3c167346a', 'bb6edd71eb924aad8254f973fb5481e4',
              'c1b561d9a1e54a7d8756519fbcff8f3b', '9c027fb3e7f749818f0fa544fb0cfcc1',
              'bbde30e11fc543d7ba04e3c8f1ca7ec7', '0ecd76655ef44a19b7128196944db4be',
              '2436ce9619d84adcbc8549beb78bd6d5', '03b990abeab14e3684068c941cbdb87e',
              '61610731669e4161b92d67c180260c3d', '76b4ce69aca6454d9c72e32c1e9dab30',
              'f59ee1b103844533a6d58af452c5a0c7', 'd0eb58d062304664864c5f6f0a0dae10',
              '7c405c942eee4c87976296856dd05508', 'e3500d43f07c40a8b3fe52e4917abb17',
              'f8c960ba775a4e91bcd517d992785521', '454678f055eb43fb9c5f2541732d2b93',
              '237c61da7646453fae261732c1298bcb', '9de8a8e8849b46d9a32ca6492fe1545a',
              '34ce9d0bc1ec49b8bce0a0b94715a33e', '054e1426c62b425e89be80661f17b456',
              '9dc150f712c9415e85b23d9f34d601a7', 'e70f3dc3b70a48b3a86d85878365918a',
              '15b085e46d5f42a7b999c608edb1c632', 'bf322332a86745ccb1c5619977955879',
              '5c8b32ead77e4c50bc70f304f1e9868f', '13219253b2df4443b0ab43de4d4e1516',
              'c1609ee6bd9b48fca040c2fe5dbf6bac', '1ac2e202a4a14aaeb575ed25972ab4d1',
              'd2195ea92ce54ee481fe6adf2a0dda47', '7c50867af99d408c83b1d6ec5e2df440',
              'a98f4f0ab16a4bc7b0b0cb70d0f1a381', '8af418b91cae49be9e8a127fa4861df5',
              'd407aff10fbe443e90ffead0647150d8', 'd4d41e484aa640768c8aad95f2ad0bfb',
              'fffee741a880456a93f746d24e284615', '8b5f14d7bcdb4067a4b925257f03f61f',
              '2626494bccdc4bdbba14f5560f133f63', '6a62cab539f14147a039095a87e2421c',
              '85857e1097394466b118158636b7fd2e', 'c09e288b81034563a90228fa53bbe32f',
              '6e27819175bb45ac85d467a597fdeec0', '81a1ed9b30b843dbbcef822c74b35257',
              'a9f8e86aa9074e43a42ce72e15a7f83f', 'a6a3b09789c44cc4ab4dccc61ebaab8d',
              'ee6791ce41a149f4ac2b6df57850a9a8', '4431ed1d5dde4419ad6116983b15eaab',
              '410b4cfb60444431892e14235f87ab2f', '9ba35205387c4a9ba8459d2af3641cff',
              '8d982f88abb240449cb017ad832fb09c', 'ce6ed3850c39437e93eb67d01475f514',
              '1164ea9e2c684c39933816d66d13abee', '705ba30800b841908276ec8407592c96',
              '3b2a732eb47d4966a5ae221bdf058b43', 'ebf4c0e7ee0c433c841e2a3d0c074109',
              'f308549556be416b86e7289c507edc5d', '303635975608442c8579e97f6202e79d',
              '1d2b3a628c6841d5b87d201237452cd4', '869d921b0520456db1118d7a3cff928d',
              '37996521c978456081a6dd0f3378f2e6', '5af132e03d2b4a69b51a7358c2c960aa',
              'db4fa4e4a8624ea49398ae84e2e13a9e', 'd7f8ae17b0ee4db79e6e53872896c836',
              '96bb675c17764acb9cad4cef12fdffb0', '6e474a7fad584e62bdb90170e93374b3',
              '1a4e4038364246c48b79952be9d6f50a', '26e0328cd1b24032af164cc524e9137c',
              '13150ab3c68f4b22841868a2b8a79891', '19c94bbf2bd9437fb28e1691687beebb',
              'a547edb389d34f279f6140e3e026b6bc', 'ac7d3b4611df4fcb96d0a1c51ccf7437',
              'd7c84926c66241b7b45a868e7118fb5f', 'd1b1f4a5736548f8bc1bced93075ca8f',
              'c92aac70d3854828a80f0d2e39efa3f8', 'a77ae945539144e7bb4ce99b1d8e22b3',
              '8ce3ad24fac14d21882ff171cb2bd685', '4c6eba78fe9140f7abcafe34d17433f8',
              '8c099f2ee5be461792c78f82f19ad29c', '2d0611a6be7041c49ef3225d0362d6fd',
              'eb001054033247fbaffca65682300b11', '730725d055054f4f86c6b23220deeec0',
              '043f35edd51445f4bee5f7b9e805d80b', '33c16f6e35144aabaf56d9269dfd08f7',
              '896d376fd54d4cde95764750d2588dd2', '1229eda1a62847468359af4a0081e31e',
              'df535178dd5e4738a35695f73995f10a', 'bf3c14637a0e48d890c32fc4e23b35b9',
              '9894434e590c4b2ba26e434fedd2b8f0', '6e5d63a3f14149b8b034724fd6e3fc4c',
              '0f55604e774a4e8295f86364585afb43', '468a02c45dc240f59228c3b5ff882372',
              '52e7d0670a29423a8a4ee6fe1291755e']
len1 = len(userid_lst)
for i in range(len1):
    userid_email_dist[userid_lst[i]] = email_lst[i]
# print(userid_email_dist)#userid是key,email是value

for i1 in range(len(cols)):
    if cols[i1] in MID_USERID_dic:
        lst1.append(MID_USERID_dic[cols[i1].strip()])
    else:
        lst1.append('NULL')
print(lst1)
for i2 in range(len(cols)):
    if lst1[i2] != 'NULL':
        lst2.append(userid_email_dist[lst1[i2].strip()])
    else:
        lst2.append('NULL')
print(lst2)

data_write("4.xls", lst2)
data_write("3.xls", lst1)
