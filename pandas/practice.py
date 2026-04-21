import pandas as pd 


df = pd.read_csv('/workspaces/students.csv')
#print(df)

#total = df.groupby('Name')['Score'].sum()
#subject =df.groupby('Subject')['Score'].mean()
#student = df.groupby('Name')['Score'].sum().sort_values(ascending=False)
df['Passed']=df['Score'] >=70 
passed = df.value_counts('Passed')







print(passed)
#print(df.head())
#print(total)
#print(subject)
#print(student.to_string())
