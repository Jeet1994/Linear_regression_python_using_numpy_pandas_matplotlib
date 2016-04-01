
#Import all packages
import numpy as n
import pandas as p
import matplotlib.pyplot as pl

#Create dataframes
x = p.read_csv("G:\CODEWORK\LinRegressOnPython\Housing.csv",usecols=[1])
y = p.read_csv("G:\CODEWORK\LinRegressOnPython\Housing.csv",usecols=[3])

#Initialise plots
fig, vis = pl.subplots()

#Get values from DataFrames
x1 = x.values.flatten()
y1 = y.values.flatten()

#Get Regression values
reg_vals = n.polyfit(x1,y1,deg=1)

#Create Visuaisation
vis.plot(x, reg[0]*x + reg[1], color = 'green')
vis.scatter(x,y)
fig.show()

#Refer : http://matthiaseisen.com/pp/patterns/p0170/ for more idea on plotting
