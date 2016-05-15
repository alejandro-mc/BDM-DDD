#Main for the Big Data Team Data Driven Dreamers
#Rosario, Alejandro, Wendy and Bishwo
#Using Seaborn to make the graphs from the data usage

#%matlibplot
import numpy as np
import seaborn as sns
import pandas as pd



#histogram noise complaints per lot
#sns.set_style()
#compData = pd.read_csv('')
#complaints = sns.barplot()


#Histogram for the values of time of day vs. number of calls
sns.set_style("whitegrid")
dayCallsData = pd.read_csv('calls_per_hour.csv')
ldayCalls = sns.barplot(x="time", y="amount", data=dayCallsData)
sns.plt.show()

#plot of day of the year vs noise complaints
sns.set_style("whitegrid")
dayOfYearData = pd.read_csv('sortedData.csv')
dayOfYear = sns.barplot(x="date", y="amount", data=dayOfYearData)
dayOfYear.set(xticklabels=[])
sns.plt.show()

#plot of average age of neighborhood vs number of noise complaints
#sns.set_style()
#ageData = pd.read_csv('')
#ageNoiseComplaints = sns.barplot()
#ageNoiseComplaints.savefig("AverageAgeVComplaints.png")
