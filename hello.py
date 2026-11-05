import pandas as pd

data = {"pizza": ["Cheese", "Pepperoni", "Hawaiian"],
        "sold": [10, 25, 7]}

df = pd.DataFrame(data)
print(df)
print("Total sold:", df["sold"].sum())