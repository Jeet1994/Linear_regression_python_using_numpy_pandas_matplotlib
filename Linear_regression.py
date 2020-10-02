
#housing prediction first project through linear regression

import pandas as p
import numpy as n



#Setting the x and y parameters of the equation.
#Open the dataset and see for yourself what is the 1st and 3rd column.
#Here, x and y are set as dataframes.
x = p.read_csv("G:\CODEWORK\LinRegressOnPython\Housing.csv",usecols=[1])
y = p.read_csv("G:\CODEWORK\LinRegressOnPython\Housing.csv",usecols=[3])

#Here we generate the 
x = x.values
y = y.values

x = x.flatten()
y = y.flatten()

#Print x and y and check what they are for better understanding

regression_coefficients = n.polyfit(x,y,1)

#Go to the IDLE and type : regression_coefficients, and press ENTER to see
# a and b values of the straight line (Regression) equation.

#The answer will be :  1.01193571e-05,   2.27585470e+00

#thus the equation is:
#####################   y = 1.01193571e-05*x + 2.27585470e+00


