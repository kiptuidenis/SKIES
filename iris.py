#!/usr/bin/python3

"""Practice using pandas with iris dataset."""

import pandas as pd

myiris = pd.read_csv('iris.csv')
#print("The last five records for the iris dataset are:")
#print(myiris.tail())

myiris2 = pd.DataFrame(myiris) #convert to dataframe
#print(type(myiris2))


#use only 2 columns
#Y = myiris["Species"]
#print("The species column is:") 
#print(Y)

#print(Y.describe())

#print(myiris.max(axis=0))

groupiris = myiris.groupby("Species")
print(groupiris.mean())