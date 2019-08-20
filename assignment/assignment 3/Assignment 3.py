import pandas as pd
import seaborn as sns

df1=pd.read_csv('gapminder-FiveYearData.csv')  #reads the csv file
#print(df1)
#print(df1.duplicated().value_counts()) 
#checks the duplicate values and counts

df2=df1[['continent','year','lifeExp']]  
#extract the needed columns from the dataset
#print(df2)

df3=pd.pivot_table(df2,index='continent',columns='year',values='lifeExp')  #create a pivot table
print(df3)

sns.heatmap(df3,annot=True).get_figure().savefig('HeatMap.png')  
#creates a heatmap of the pivot table and saves the figure
