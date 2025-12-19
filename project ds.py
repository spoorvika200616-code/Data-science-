import pandas as pd
df=pd.read_csv("C:\\Users\\STUDENT\\Downloads\\NewCompanyDetails (2).csv")
df=df.drop_duplicates()
df=df.dropna()
df.to_csv("newdetails1.csv")
df['revenue']=df['revenue'].replace(r'[^0-9]','',regex=True)
df['total workers']=df['workers']+df['previous_workers']
df.to_csv("newfiledetails.csv")
print("dd")
