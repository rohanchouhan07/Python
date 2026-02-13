
import pandas as pd

Data={
    "Name":["Rohan","None","Ayush","Divya","Mohit","Ram","Sita","Geeta","Arham","Kapil"],
    "Age":[20,21,19,17,31,18,17,13,18,17],
    "Salary":[15200,50000,35000,45000,60000,52000,36000,95000,75000,140000],
    "Address":["Indore","Delhi","Kanpur","Delhi","Mumbai","Dhar","Ujjain","Bhopal","Delhi","Jabalpur"],
    "performance":[9,8.2,7.3,6.5,2.0,7.6,8,6.5,7.6,9.8]
}
df=pd.DataFrame(Data)
print(df)
print("\n \n")

print(df.groupby("Age")["Salary"].sum())