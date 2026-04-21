import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("/workspaces/sales_data.csv")
df['date'] = pd.to_datetime(df['date'])


print(df)

