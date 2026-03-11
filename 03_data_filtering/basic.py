import pandas as pd

data = {
    "Name": ["Rohit","Kohli","Dhoni","Gill"],
    "Age": [39,38,43,25],
    "City": ["Ahmedabad","London","Paris","Mumbai"],
    "Runs": [18000,26000,17000,4000]
}

df = pd.DataFrame(data)

# Filtering by Runs
print(df[df["Runs"]>15000])
print()

# Filtering by Age
print(df[df["Age"]<40])
print()

# Filtering by City
print(df[df["City"]=="Mumbai"])
print()

# Multiple Conditions
print(df[(df["Runs"] > 15000) & (df["City"]=="London")])
print()

print(df[(df["City"]=="Mumbai") | (df["City"]=="London")])
print()