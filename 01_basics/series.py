# Series is one-dimensional array
# It stores a single column of data

import pandas as pd

data = [100,200,300,400]
series = pd.Series(data)
print(series)

# Series With Custom Indexing
data = [100,200,300]
series = pd.Series(data,index=["a","b","c"])
print("Series with custom indexing")
print(series)
print()

# Accessing Values
data = [10,20,30]
series = pd.Series(data)
print("Accessing Values in Series")
print("Value :",series[1])
print()

# Series From Dictionary
# key -> index
# value -> data

data = {
    "Maths" : 90,
    "Science" : 85,
    "English" : 75
}
series = pd.Series(data)
print("Series from Dictionary")
print(series)
print()