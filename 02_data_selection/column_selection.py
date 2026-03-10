import pandas as pd

data = {
    "Name" : ["Rohit","Kohli","Dhoni"],
    "Age" : [39,38,43],
    "City" : ["Ahmedabad","London","Paris"]
}

df = pd.DataFrame(data)
print("Original DataFrame")
print(df)
print()

# Select single column 
print("Single Column")
print(df["Name"])
print()

# Select Multiple Columns
print("Multiple Columns")
print(df[["Name","Age"]])
