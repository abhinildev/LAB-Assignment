#finding skewness kurtosis and moments
from scipy.stats import skew,kurtosis
from scipy import stats 
import numpy as np 
l1=[]
n=int(input("Enter the no of values in the dataset"))
for i in range(0,n):
    y=float(input("Enter the dataset: "))
    l1.append(y)

s1=skew(l1,axis=0,bias=True)
print("The skewness of the given dataset is : " ,s1)
k1=kurtosis(l1,axis=0,bias=True)
print("The kurtosis of the given dataset is :",k1)
j=int(input("Enter the value of n: "))
m1=stats.moment(l1,moment=j)
print("The moment about ",j,"is :",m1)