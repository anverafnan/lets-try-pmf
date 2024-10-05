import scipy.stats as stats
prob_1=stats.binom.pmf(4,10,0.5)
print("Probablity of getting 4 heads: ",prob_1)
prob_2=1-stats.binom.pmf(0,n=10,p=0.5)-stats.binom.pmf(1,10,0.5)-stats.binom.pmf(2,10,0.5)
print("Probablity of getting two heads: ",prob_2)