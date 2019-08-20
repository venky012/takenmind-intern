import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series1 = Series([10,20,30,40],index=['a','b','c','d'])
print series1

index1 = series1.index
print index1

print index1[2:]

#negative indexes
print index1[-2:]
print index1[:-2]

print index1[2:4]

#interesting
index1[0] = 'e'
print index1