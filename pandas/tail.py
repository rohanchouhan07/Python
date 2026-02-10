import pandas as pd

df=pd.read_csv('sales_data_sample.csv',encoding='latin1')
print(df.tail(10))# 10 should be changalbe accoeding to row default value is 5