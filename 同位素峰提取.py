'''首先对质量数按照升序排序'''

import pandas as pd
import numpy as np
#读取需要处理的excel
peak_df = pd.read_excel(r'H:\峰表结果.xlsx')
shapeMax = peak_df.shape[0]
peak_after_df = pd.DataFrame(np.nan, index=range(shapeMax),
                              columns=range(100))

for i in range(0,shapeMax-1000):
        print(i)
        num=0
        mz_peak1 = peak_df.iloc[i,2]
        for l in range(i,i+1000):
            mz_peak2 = peak_df.iloc[l,2]
            #同位素差值
            mass_error = (10**6)*abs(mz_peak2-mz_peak1--1.99705)/(mz_peak2)
            #质量误差ppm<10 ppm
            if mass_error < 10:
                rt_peak1 = peak_df.iloc[i, 1]
                rt_peak2 = peak_df.iloc[l, 1]
                rt_error = abs(rt_peak1 - rt_peak2)
                #时间误差<0.2 min
                if rt_error < 0.1:
                    height_peak1 = peak_df.iloc[i, 3]
                    height_peak2 = peak_df.iloc[l, 3]
                    height_rate = height_peak2 / height_peak1
                    #峰强比例 0.5 < height_rate < 2
                    if 0.3 < height_rate < 0.4:
                            num = num+1
                            peak_location = 4*num-4
                            ppm_location = peak_location+1
                            tr_location = peak_location+2
                            height_rate_location = peak_location+3
                            peak_after_df.iloc[i,peak_location] = mz_peak2
                            peak_after_df.iloc[i, ppm_location] =  mass_error
                            peak_after_df.iloc[i, tr_location] = rt_error
                            peak_after_df.iloc[i, height_rate_location] = height_rate
for i in range(shapeMax-1000,shapeMax):
        print(i)
        num=0
        mz_peak1 = peak_df.iloc[i,2]
        for l in range(i,shapeMax):
            mz_peak2 = peak_df.iloc[l,2]
            #同位素差值
            mass_error = (10**6)*abs(mz_peak2-mz_peak1---1.99705)/(mz_peak2)
            #质量误差ppm<10 ppm
            if mass_error < 10:
                rt_peak1 = peak_df.iloc[i, 1]
                rt_peak2 = peak_df.iloc[l, 1]
                rt_error = abs(rt_peak1 - rt_peak2)
                #时间误差<0.2 min
                if rt_error < 0.1:
                    height_peak1 = peak_df.iloc[i, 3]
                    height_peak2 = peak_df.iloc[l, 3]
                    height_rate = height_peak2 / height_peak1
                    #峰强比例 0.2 < height_rate < 2
                    if 0.3 < height_rate < 0.4:
                            num = num+1
                            peak_location = 4*num-4
                            ppm_location = peak_location+1
                            tr_location = peak_location+2
                            height_rate_location = peak_location+3
                            peak_after_df.iloc[i,peak_location] = mz_peak2
                            peak_after_df.iloc[i, ppm_location] =  mass_error
                            peak_after_df.iloc[i, tr_location] = rt_error
                            peak_after_df.iloc[i, height_rate_location] = height_rate

peak_after_df.dropna(axis=1,how='all',inplace=True)
df=pd.concat([peak_df,peak_after_df],axis=1)
df.to_csv(r'H:\同位素峰结果.csv',index=False)







