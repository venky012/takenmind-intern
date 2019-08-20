import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series

ds = randn(100)
# fig = sns.distplot(ds, bins=15).get_figure()
# fig.savefig('image1.png')

# fig2 = sns.distplot(ds,hist=False,rug=True,bins=10).get_figure()
# fig2.savefig('image2.png')

#change parameters of each graph

# fig3 = sns.distplot(ds,bins=15,
#                     kde_kws= {'color':'red','label':'KDE graph'},
#                     hist_kws={'label':'Histogram Label', 'color':'green','alpha':0.5}
#                     ).get_figure()
# fig3.savefig('image3.png')

s1 = Series(ds,name='s1')

fig4 = sns.distplot(s1,bins=15).get_figure()
fig4.savefig('image4.png')





