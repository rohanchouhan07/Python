
"""
# !vertically (Row=wise) 
# *Horizontalyy(column wise)

[df1,df2]=
axis=1
"""
import pandas as pd
df1={
    "Customer_id":[1,2,3,4,5],
    "Name":["ROhan","Mohan","sohan","Kalpesh","Kapil"]
}
df2={
    "Customer_id":[1,2,3,4,5],
    "Amount":[250,360,240,300,120]
}
df=pd.DataFrame(df1)
df3=pd.DataFrame(df2)

df_Concatnitae=pd.concat([df,df3],axis=1,ignore_index=True)
print(df_Concatnitae)