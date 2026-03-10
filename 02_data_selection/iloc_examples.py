import pandas as pd

data = {
    "Name" : ["Rohit","Kohli","Dhoni"],
    "Age" : [39,38,43],
    "City" : ["Ahmedabad","London","Paris"] 
}

df = pd.DataFrame(data)

print(df.iloc[1])
