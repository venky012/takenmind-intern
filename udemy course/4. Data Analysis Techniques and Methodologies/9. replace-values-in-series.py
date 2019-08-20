import numpy as np
import pandas as pd
from pandas import Series,DataFrame

s1 = Series([10,20,40,50,20,10,50,40])
print s1

print s1.replace(50,np.nan)

print s1.replace([10,20,50],[100,200,500])

print s1.replace({10:100,20:np.nan,40:400})

