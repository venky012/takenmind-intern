import numpy as np
import pandas as pd
from pandas import DataFrame

df = DataFrame({ 'country': ['Afghanistan','Albania','Algeria'],
                 'code':['93','355','213']})
print df

GDP_map = {'Afghanistan': '20', 'Albania': '12.8','Algeria':'215'}

print GDP_map

df['GDP'] = df['country'].map(GDP_map)

print df