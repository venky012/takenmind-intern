import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mean = [0,0]
covariance = [[1,0],[0,100]]

ds = np.random.multivariate_normal(mean,covariance,500)

dframe = pd.DataFrame(ds, columns=['col1','col2'])

fig = sns.kdeplot(dframe).get_figure()
fig.savefig('kde1.png')

#shade
fig2 = sns.kdeplot(dframe,shade=True).get_figure()
fig2.savefig('kde2.png')

#bandwith change
fig3 = sns.kdeplot(dframe,bw='silverman').get_figure()
fig3.savefig('kde3.png')

#kind variable
fig4 = sns.jointplot('col1','col2',dframe,kind='kde')
fig4.savefig('kde4.png')

