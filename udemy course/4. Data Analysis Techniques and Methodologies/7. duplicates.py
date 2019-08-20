import pandas as pd
from pandas import DataFrame

df = DataFrame({
    'col1':['uber','uber','uber','uber','grab'],
    'col2':[5,4,3,3,5]
})

print df

print df.duplicated()

print df.drop_duplicates()

print df.drop_duplicates(['col1'])

print df.drop_duplicates(['col1'] , keep='last')

