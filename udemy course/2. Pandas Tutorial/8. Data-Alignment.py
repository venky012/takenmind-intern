import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser_a = Series([100,200,300],index=['a','b','c'])
ser_b = Series([300,400,500,600],index=['a','b','c','d'])

#sum of series
print ser_a+ser_b

#dataframe
df1 = DataFrame(np.arange(4).reshape(2,2),columns=['a','b'],index=['car','bike'])
print df1
df2 = DataFrame(np.arange(9).reshape(3,3),columns=['a','b','c'],index=['car','bike','cycle'])
print df2
print df1+df2

df1 = df1.add(df2,fill_value=0)
print df1

ser_c = df2.ix[0]
print df2 - ser_c
