import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.arange(25).reshape(5,5), index=['UBER','OLA','GRAB','GOJEK','LYFT'], columns=['RE','LO','QU','GR','AG'])

print df

#way1 -  use mapping
df.index = df.index.map(str.lower)
print df

#way2 - rename method
print df.rename(index=str.title,columns=str.lower)

#way3 of using doctionary
print df.rename(index={'uber':'The Best Taxi'}, columns={'RE':'Revenue'})

#how to save
df.rename(index={'uber':'The Best Taxi'}, columns={'RE':'Revenue'},inplace=True)

print df