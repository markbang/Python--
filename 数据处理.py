import pandas as pd
df=pd.read_csv('score.csv')
print(df.groupby('uOccup').size())
print(df.groupby('uOccup').count())