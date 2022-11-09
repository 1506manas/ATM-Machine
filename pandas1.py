import pandas as pd
df=pd.read_csv("example.csv")
df.set_index('Units Sold',inplace=True)

print(df)
