#Sort CSV data files

import datetime

data = []
with open('DataResults/calls_per_day.csv') as input: 
    for line in input:
        data.append(line)
data.sort(key=lambda x: datetime.datetime.strptime(x.split(',')[0], "'%m/%d/%Y'"))

for line in data:
    print line.strip()
        