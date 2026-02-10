import pandas as pd

Data={
    "Name":["Rohan","Krish","Ayush","Divya","Mohit","Ram","Sita","Geeta","Arham","Kapil"],
    "Age":[20,21,19,17,21,18,17,13,18,17],
    "Salary":[100000,50000,35000,45000,60000,52000,36000,95000,75000,140000],
    "Address":["Indore","Delhi","Kanpur","Dewas","Mumbai","Dhar","Ujjain","Bhopal","Delhi","Jabalpur"],
    "performance":[9,8.2,7.3,6.5,2.0,7.6,8,6.7,7.6,9.8]
}
df=pd.DataFrame(Data)
print(df)
print(f'Shape : {df.shape}')
print(f'Column Name :{df.columns}')