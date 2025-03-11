#!/usr/bin/python3

"""Practice using pandas with iris dataset."""

import pandas as pd

myiris = pd.read_csv('iris.csv', usecols=["SepalLengthCm", "Species"])
#print("The last five records for the iris dataset are:")
#print(myiris.tail())

#use only 2 columns
Y = myiris["Species"]
#print("The species column is:") 
#print(Y)

print(myiris.describe())