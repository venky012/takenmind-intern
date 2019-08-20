import pandas as pd
from pandas import Series
import numpy as np
object = Series([5,10,15,20])
print (object)

print (object.values)
print (object.index)


#use numpy arrays to series
data_array = np.array(['a','b','c'])
s = Series(data_array)
print (s)

#custom index
s = Series(data_array,index=[100,101,102])
print (s)
s= Series(data_array,index=['index1','index2','index3'])
print (s)


#using real life ex

revenue = Series([20,80,40,35],index=['ola','uber','grab','gojek'])

print (revenue['ola'])
print (revenue[revenue>=35])

#use boolean conditions

print ('lyft' in revenue)

revenue_dict = revenue.to_dict()
print (revenue_dict)

#nan values
index_2 = ['ola','uber','grab','gojek','lyft']
revenue2 = Series(revenue,index_2)
print (revenue2)

print (pd.isnull(revenue2))

print (pd.notnull(revenue2))

#addition of series (+)

print (revenue+revenue2)

#assigning names
revenue2.name="Company Revenues"
revenue2.index.name="Comapany Name"
print (revenue2)