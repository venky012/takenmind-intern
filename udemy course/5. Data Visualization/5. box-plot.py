import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds1 = randn(80)
#sns.boxplot(ds1, orient='v').get_figure().savefig('box1.png')
sns.boxplot(ds1,whis=np.inf).get_figure().savefig('box2.png')

