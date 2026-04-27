import pandas as pd 
import matplotlib.pyplot as plt 


df=pd.read_csv('/workspaces/csv/tlelve.csv')

#datetime
df['date'] = pd.to_datetime(df['date'])

#cleaning data
df["visitors"] = df["visitors"].fillna(df["visitors"].mean())
df = df.dropna(subset=["orders"])
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["revenue"] = df["revenue"].fillna(df["revenue"].mean())

df['conversion rate'] = df['visitors'] / df['orders']

#Total revenue
total_revenue = df['revenue'].sum()

print('Toral revenue is',total_revenue)

#Average daily visitors

average_visitors = df['visitors'].mean()

print('Average daily visitors is', average_visitors)

#Day with highest revenue
max_row = df.loc[df['revenue'].idxmax()]

print('Highest revenue was', max_row['revenue'], 'on', max_row['date'])



#Line chart revenue over time

#Bar chart total orders per week

#Scatter plot visitors vs revenue