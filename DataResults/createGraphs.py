#Main for the Big Data Team Data Driven Dreamers
#Rosario, Alejandro, Wendy and Bishwo
#Using Seaborn to make the graphs from the data usage

#%matlibplot
import numpy as np
import seaborn as sns
import pandas as pd



#ScatterPlot Property Value vs noise complaints per unit  
sns.set_style("whitegrid")
compData = pd.read_csv('propvalue_vs_noise_per_resunit.csv')

complaints = sns.lmplot(x="propertyValue", y="callsperunit", data=compData, fit_reg=False)
complaints.set(yscale= "log")
sns.plt.show()

#ScatterPlot Property Value vs construction complaints per unit  
sns.set_style("whitegrid")
compData = pd.read_csv('val_vs_constcomp.csv')

complaints = sns.lmplot(x="propertyValue", y="callsperunit", data=compData, fit_reg=False)
complaints.set(yscale= "log")
sns.plt.show()

#ScatterPlot Property Value vs party complaints per unit  
sns.set_style("whitegrid")
compData = pd.read_csv('value_vs_partycomp.csv')

complaints = sns.lmplot(x="propertyValue", y="callsperunit", data=compData, fit_reg=False)
complaints.set(yscale= "log")
sns.plt.show()


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
