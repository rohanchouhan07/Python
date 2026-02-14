# pd.merge(df1,df2,on="Column_name",how="Type of join")
import pandas as ps

df1={
    "Customer_id":[1,2,3,4,5],
    "Name":["ROhan","Mohan","sohan","Kalpesh","Kapil"]
}
df2={
    "Customer_id":[1,2,3,4,5],
    "Amount":[250,360,240,300,120]
}
df=ps.DataFrame(df1)
df3=ps.DataFrame(df2)
print(df,"\n ")
print(df3,"\n \n")
print(ps.merge(df,df3,on="Customer_id",how="inner"))
print(ps.merge(df,df3,on="Customer_id",how="right"))
print(ps.merge(df,df3,on="Customer_id",how="left"))