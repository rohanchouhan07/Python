# import library
import pandas as pd
import numpy as np

# loading the file
df = pd.read_csv("C:/Users/rohan/OneDrive/Desktop/pyhton/projects/numpy and pandas/Indian_Employee_Data.csv", encoding="utf-8")

# see the head
print(df.head())

# checking the missing values
print("Missing value in each column",)
print(df.isnull().sum())

# filling the missing data 
df.fillna({"Salary": df["Salary"].mean()}, inplace=True)
df.fillna(df["Age"].interpolate(),inplace=True)
df.fillna(df["Experience_Years"].interpolate(),inplace=True)
df.fillna(df["Performance_Rating"].interpolate(),inplace=True)
df["State"]=df["State"].fillna(df["State"].mode()[0],inplace=True)
df["Department"]=df["Department"].fillna(df["Department"].mode()[0],inplace=True)
df["Position"]=df["Position"].fillna(df["Position"].mode()[0],inplace=True)
df["Joining_Date"]=df["Joining_Date"].fillna(df["Joining_Date"].mode()[0],inplace=True)

# 1. Replace infinities with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# 2. Fill NaNs with the mean of each column
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# drop dublicates
df.drop_duplicates(inplace=True)

# do Nagative salary in a positive interger
df["Salary"]=np.where(df["Salary"]<0,df["Salary"].mean(),df["Salary"])

# set the boundary of salary 
salary_mean=df["Salary"].mean()
salary_std=df["Salary"].std()
lower_bound=salary_mean-(3*salary_std)
upper_bound=salary_mean+(3*salary_std)
df=df[(df["Salary"]>= lower_bound) & (df["Salary"] <= upper_bound)] 
print("Missing value in each column after clining",)
print(df.isnull().sum(),"\n")

# ! PRINT The cheaned data
print("See the whole data ")
print(df)

df.to_csv("Cleaned_Data_Indian_Employee.csv ",index=False)

print("Data cleaned succesfully")

