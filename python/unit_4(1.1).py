import pandas as pd

data = [18, 97, 38, 61, 6, 15]
series = pd.Series(data)
list_data = series.tolist()

print(list_data)
print(type(list_data))
