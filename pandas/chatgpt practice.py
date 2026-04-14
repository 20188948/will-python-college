import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/workspaces/codespaces-blank/customers-1000.csv')
df.head()


#print(pd.DataFrame(df))
counts =df['Country'].value_counts()
counts = counts[counts > 7].reset_index()
counts.columns = ['Country', 'Count']
print(counts)

xpoints =df['Country']
ypoints = df['City']

plt.plot(xpoints,ypoints,'o')
plt.xlabel('Country')
plt.ylabel('City')
plt.title('City by Country')


print(plt.show())
plt.savefig('Graph.png')