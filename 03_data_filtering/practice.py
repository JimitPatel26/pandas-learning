import pandas as pd
# Task 1
# Print only the Name column.

data = {
    "Name": ["Rohit","Kohli","Dhoni","Gill"],
    "Age": [39,38,43,25],
    "City": ["Ahmedabad","London","Paris","Mumbai"],
    "Runs": [18000,26000,17000,4000]
}

df = pd.DataFrame(data)
print(df["Name"])
print()

# Task 2
# Print 2 columns Name and Runs
print(df[["Name","Runs"]])
print()

# Task 3
# Print the row with index 2.
print(df.loc[2])
print()

# Print rows from index 0 to 2
print(df["Name"].loc[0:2])

# Print the second row using iloc.
print(df.iloc[1])
print()

# Print players with: Runs > 20000
print(df[df["Runs"]>20000])
print()

# Question 7 🟠 (Filtering) Print players with : Age < 40
print(df[df["Age"]<40])
print()

# Question 8 🔴 (Harder) Print players where: Runs > 15000 AND Age < 40
print(df[(df["Runs"]>15000) & (df["Age"]<40)])
print()

# Question 9 🔴 (Harder) Task : Print players where : City is Mumbai OR City is London
print(df[(df["City"]=="Mumbai") | (df["City"]=="London")])
print()

# Question 10 🔥 Task Print only Name and Runs for players where: Runs > 15000
print(df[df["Runs"]>15000][["Name","Runs"]])
print()

data = {
    "Name": ["Rohit","Kohli","Dhoni","Gill","Rahul","Pant"],
    "Age": [39,38,43,25,32,27],
    "City": ["Ahmedabad","London","Paris","Mumbai","Delhi","Mumbai"],
    "Runs": [18000,26000,17000,4000,8000,6000],
    "Matches": [450,500,350,80,200,120]
}

df = pd.DataFrame(data)

# Print players where : Runs > 10000
print(df[df["Runs"]>10000])
print()

# Print only Name and Runs for players where:
print(df[df["Matches"]>200][["Name","Runs"]])
print()

# Print players where : City == "Mumbai" But only show columns : Name , Age
print(df[df["City"]=="Mumbai"][["Name","Age"]])
print()

# Print players where:  Age < 4  AND  Runs > 10000
print(df[(df["Age"]<40) & (df["Runs"]>10000)])
print()

# Print players where: City == "Mumbai" OR Runs > 20000

df["StrikeRate"] = df["Runs"] / df["Matches"]
print(df)