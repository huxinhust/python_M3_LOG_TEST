# -*- coding: UTF-8 -*-
import numpy as np
# import demjson
import os
# import json
import time
import math
# # import matplotlib.pyplot as plt
# # import math
# # import string
# # import seaborn as sns
# # from pylab import *
# # from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# # from scipy import stats
# # import pandas as pd
# # fp = open("C://Users/dou/Desktop/1/naming-server-standalone.log")
# # for line1 in fp.readlines():
# #     if line1.startswith('{"info'):
# #         line1=json.loads(line1)
# #         print(line1)
# #         #print(type(line1))
# 使用time
# timeStamp = 1557144309204/1000
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
# print(otherStyleTime)   # 2013--10--10 23:40:00
# start_time0 = '2019-04-22 00:00:00'
# end_time0 = '2019-04-22 01:01:00'
# timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
# timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
# start_timeStamp = 1000 * int(time.mktime(timeArray1))
# end_timeStamp = 1000 * int(time.mktime(timeArray2))

# print(start_timeStamp)
# import math
#
#
#
#
#
# #print(panduan_shijianduan(end_timeStamp))
# start_time0 = '2019-04-30 00:00:00'
# end_time0 = '2019-05-01 03:59:59'
# timeArray1 = time.strptime(start_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
# timeArray2 = time.strptime(end_time0, "%Y-%m-%d %H:%M:%S")  # 时间戳
# start_timeStamp = 1000 * int(time.mktime(timeArray1))
# end_timeStamp = 1000 * int(time.mktime(timeArray2))
# bin1=4*60*60*1000
# print(math.ceil((end_timeStamp-start_timeStamp)/bin1))
import pandas as pd
import numpy as np
dti=pd.date_range(start='2019-04-30 00:00',end='2019-05-04 23:59', freq='4H')
pydate_array = dti.to_pydatetime()
date_only_array = np.vectorize(lambda s: s.strftime('%Y-%m-%d  %H:%M'))(pydate_array )
date_only_series = pd.Series(date_only_array)
print(date_only_series[1])








