import pandas as pd

data = {
    "Name" : ["Rohit","Kohli","Dhoni"],
    "Age" : [39,38,43],
    "City" : ["Ahmedabad","London","Paris"]
}

df = pd.DataFrame(data)
print(df)
print()

# Accessing a Column
print("Accessing a Column")
print(df["Name"])
print()

# Accessing a Column
print("Accessing more Columns")
print(df[["Name","Age"]])
print()

# Accessing a row
print("Accessing row")
print(df.loc[1])

# First 5 rows
print(df.head())
print()

# rows and columns (m,n) returns tuple
print(df.shape)
print()
# Real World Use Case

df = pd.read_csv("01_basics\\products.csv")
print(df)