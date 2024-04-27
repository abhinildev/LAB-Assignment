import matplotlib.pyplot as plt 
from scipy.stats import binom
n=int(input("Enter the number of occurences: ")) 
p=float(input("Enter the probability of success: "))
if p>1:
    print("Invalid input")
    exit(0) 
    
r_values=list(range(n+1))

mean,var=binom.stats(n,p)

dist=[binom.pmf(r,n,p) for r in r_values]

print("r\tp(r)")
for i in range(n + 1): 
    print(str(r_values[i]) + "\t" + str(dist[i]))
    
print("mean :" +str(mean))

print("variance: "+str(var))
#plotting the distribution
plt.bar(r_values,dist)
plt.show()
