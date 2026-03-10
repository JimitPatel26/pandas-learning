import pandas as pd

data = {
    "Name" : ["Rohit","Kohli","Dhoni"],
    "Age" : [39,38,43],
    "City" : ["Ahmedabad","London","Paris"] 
}

df = pd.DataFrame(data)

print(df)
print()

print("Selecting Row using loc")
print(df.loc[1])
print()

print("Selecting Row and Column")
print(df.loc[1,"Name"])
print()

print(df.loc[0:2])
print()

print(df.loc[0:2,["Name","Runs"]])
print()

