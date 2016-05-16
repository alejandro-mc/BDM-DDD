#Sort Data to get Correlation Coefficient
from scipy.stats.stats import pearsonr
import numpy

propValue = []
NumCallsperUnit =[]
with open('propvalue_vs_noise_per_resunit.csv') as input: 
    for line in input:
        propValue.append(float(line.split(',')[0]))
	NumCallsperUnit.append(float(line.split(',')[1]))

#calculate correlation coefficient using numpy 
#corCoef = numpy.corrcoef(propValue, NumCallsperUnit)[0,1]

corCoef = pearsonr(propValue, NumCallsperUnit)

propValue2 = []
constComp = []
with open('val_vs_constcomp.csv') as input:
    for line in input:
        propValue2.append(float(line.split(',')[0]))
        constComp.append(float(line.split(',')[1]))
	
corCoef2 = pearsonr(propValue2, constComp)

propValue3 = []
partyComp = []
with open('value_vs_partycomp.csv') as input:
    for line in input:
        propValue3.append(float(line.split(',')[0]))
        partyComp.append(float(line.split(',')[1]))
	
corCoef3 = pearsonr(propValue3, partyComp)

print corCoef
print corCoef2
print corCoef3

