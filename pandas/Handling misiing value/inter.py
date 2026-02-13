# interpulation it can find the astimated value 
# like [1,2,None,4,5,6]
# it can replace the none with 3
# it can avoid the data loss,smooth trends and preserve data integrity


import pandas as pd

Data={
    "Name":["Rohan","None","Ayush","Divya","Mohit","Ram","Sita","Geeta","Arham","Kapil"],
    "Age":[20,21,19,17,None,18,17,13,18,17],
    "Salary":[None,50000,35000,45000,60000,52000,36000,95000,75000,140000],
    "Address":["Indore","Delhi","Kanpur","None","Mumbai","Dhar","Ujjain","Bhopal","Delhi","Jabalpur"],
    "performance":[9,8.2,7.3,6.5,2.0,7.6,8,None,7.6,9.8]
}
df=pd.DataFrame(Data)
print(df)
# linear,plynomial,time
df["Age"]=df["Age"].interpolate(method="linear",axis=0,inplace=True)
print(df)

