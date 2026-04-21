import pandas as pd 
import matplotlib.pyplot as plt





df =pd.read_csv('/workspaces/sales.csv')

#df['Revenue'] =df['Units_Sold']*df['Price']
#df.groupby("Category")["Revenue"].sum()




#revenue= df.groupby('Product')['Units_Sold']['Price'].sum()



my_collum = df[['Category','Units_Sold',]]

my_dataframe = pd.DataFrame(my_collum)


print(my_dataframe)


