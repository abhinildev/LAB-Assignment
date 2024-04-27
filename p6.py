from scipy.stats import norm
import numpy as np  
import matplotlib.pyplot as plt 
#info
mean=float(input("Enter the mean of the distribution: "))
sd=float(input("Enter the standard deviation: "))
n=int(input("Enter the total no of occurences: "))
up=float(input("Enter the upper bound: "))
#z value calculation
z= (up - mean) / sd
prob=norm.cdf(z)
per=prob*100
print("Percentage of probability less than ",up,"is :",per)
#plotting the data
values = np.random.normal(mean, sd, n)
plt.hist(values, 100)
plt.axvline(values.mean(), color='k', linestyle='dashed', linewidth=2)
plt.show()