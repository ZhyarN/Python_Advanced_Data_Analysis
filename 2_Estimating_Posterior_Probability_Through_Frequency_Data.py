#We arrange a senario in which we have a data from a population of infected/healthy, and their respective 
#test results. And try to determine the likelihoods from these data for False Positive/Negative rates

import numpy as np


#Randomized Data
population=np.random.rand(8000000)#defining the population number
populant=[True if i <0.001 else False for i in population]#defining that %0.1 of the population is infected

#We make test for each member of the population, with the test having 5% chance of False Positive and 3% chance of False Negative
test=np.random.rand(8000000)
for i in range(len(test)):
    if populant[i]==False and test[i]<=0.05:
        test[i]=True
    elif populant[i]==False and test[i]>0.05:
        test[i]=False
    elif populant[i]==True and test[i]<=0.97:
        test[i]=True
    elif populant[i]==True and test[i]>0.97:
        test[i]=False


#We count the number of instances of True/False Positives and True/False Negatives 
TP=0
TN=0
FP=0
FN=0

for i in range(len(populant)):
    if populant[i]==False and test[i]==False:
        TN=TN+1
    elif populant[i]==False and test[i]==True:
        FP=FP+1
    elif populant[i]==True and test[i]==False:
        FN=FN+1
    elif populant[i]==True and test[i]==True:
        TP=TP+1

#Through the count, we arrive at the probabilities
print('All the ratios in count number and percentage:\nTrue Positive, True Negative, False Positive, False Negative')
print(TP, TN, FP,FN,'\n',TP*100/len(populant), TN*100/len(populant), FP*100/len(populant), FN*100/len(populant))

