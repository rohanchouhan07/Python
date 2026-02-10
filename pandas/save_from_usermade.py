import pandas as pd

data={
    "Name":["rohan","divya","Krish"],
    "Age" :[20,30,10],
    "city":["Indore","Mumbai","Delhi"]
}
df=pd.DataFrame(data)
print(df)
df.to_json("output.xlsx",index=False)