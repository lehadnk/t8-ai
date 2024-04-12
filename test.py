import pandas as pd
import numpy as np

data = pd.read_csv("kc_house_data.csv")

y = data["price"].apply(lambda x: int(10000 * round(float(x) / 10000)))

total = 0
ones = []
for c, v in y.value_counts().items():
    if v == 1:
        ones.append(c)
    total += v

indieces_to_remove = [k for k, v in y.items() if v in ones]

data = pd.read_csv("kc_house_data.csv")
[data.drop(i, axis=0, inplace=True) for i in indieces_to_remove]
y = data["price"].apply(lambda x: int(10000 * round(float(x) / 10000)))
X = data[["bedrooms", "waterfront", "sqft_living"]]

print(len(y), len(X))