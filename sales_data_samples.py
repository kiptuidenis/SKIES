"""
Use sales Dataset

read a csv file -- Done
read csv with specific colums 
read and describe a dataframe
select specific columns and rows 
filter data
modify data: drop columns
drop rows
manipulate data: use apply
Group by
"""
import pandas as pd

#read a csv file

#read a csv file
sales = pd.read_csv('sales_data_sample.csv', encoding='latin1') #latin1 is used for encoding

#print(sales)

#read csv with specific columns
sales2 = pd.read_csv('sales_data_sample.csv', encoding='latin1', usecols=['ORDERNUMBER', 'ORDERDATE', 'CITY', 'COUNTRY'])
#print(sales2)

#read and describe a dataframe
#print(sales2.describe())

#select specific columns and rows
#print(sales2.iloc[0:5, 0:5])
#print(sales2.iloc[2:5, 1:3])

#select cancelled orders
cancelled_orders = sales2[sales['STATUS'] == 'Cancelled']
#print("""The cancelled orders are:""")
#print(cancelled_orders)

#drop columns
sales2 = sales2.drop(columns=['ORDERNUMBER'])
#print(sales2)

#drop rows
sales2 = sales2.drop([0, 1, 2])
#manipulate data: use apply
#convert ORDERDATE to datetime
sales2['ORDERDATE'] = pd.to_datetime(sales2['ORDERDATE']) 
#print(sales2)

#Filter sales data to remain with Country column and quantity Ordered column only
sales3 = sales[['COUNTRY', 'QUANTITYORDERED']]

#Group  by country
grouped_sales = sales3.groupby('COUNTRY')
print(grouped_sales)

grouped_sales.sum()

#Sort the data in descending order
sorted_sales = grouped_sales.sum().sort_values(by='QUANTITYORDERED', ascending=False)

#save the grouped data to a csv file
sorted_sales.to_csv('grouped_sales.csv')
