import pandas as pd
salesdf = pd.read_csv("sales_data.csv")


#prints first 5 rows of data.
print(salesdf.head(),"\n")


#prints the total null values of each column
print(salesdf.isna().sum(),"\n") 


#shows the numerical data mean std min max and all
print(salesdf.describe(),"\n")

#prints the all the column headings.
print(list(salesdf.columns) ,"\n")