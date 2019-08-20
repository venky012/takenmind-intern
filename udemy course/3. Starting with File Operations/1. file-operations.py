## OBJECTIVE ##
#importing csv as dataframe
#using readtable of pandas
#reading partial rows of a csv file
#dumping data into a new csv file
#selecting specific columns of a csv file

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.read_csv('demo.csv',header=None)
print dframe

#use readtable
dframe2 = pd.read_table('demo.csv',sep=',',header=None)
print dframe2

#partial rows importing
print pd.read_csv('demo.csv',nrows=2,header=None)

#dump
dframe2.to_csv('outputCSV.csv', sep='!');

#select specific columna
dframe.to_csv('dataoutput.csv',columns=[0,1])

