import pandas as pd
import numpy as np
arr=['a','b','c','d','e','f','g']
d={'animal':pd.Series(['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog']),
              'age': pd.Series([2.5,3.0,0.5,np.nan,5.0,2.0,4.5,np.nan,7.0,3.0]),
              'visits': pd.Series([1,3,2,3,2,3,1,1,2,1]),
              'priority': pd.Series(['yes','yes','no','yes','no','no','no','yes','no','no'])}
df=pd.DataFrame(d)
df.index=list('abcdefghij')
#填充缺失值（原地修改）
df.fillna('0',inplace=True)#error1
#f行的age改为1.5
df.loc['f']['age']=1.5#error2
print(df)