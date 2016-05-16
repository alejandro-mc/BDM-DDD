##Imports
import pyspark
import sys
import operator
import csv

#Table SF-P1 CT Total Polpulation By 5 Year Age Groups

#0  Borough,2010 Census FIPS County Code,2010 DCP Borough Code,2010 Census Tract,
#4  Total Population,Under 5 Years,5-9 Years,10-14 Years,15-19 Years,20-24 Years,
#10 25-29 Years,30-34 Years,35-39 Years,40-44 Years,45-49 Years,50-54 Years,
#16 55-59 Years,60-64 Years,65 Years and Over,Median Age


def ct2010Mapper(record):
    for line in record:
        for item in csv.reader([line]):
            list_line = item
        if list_line[0] == 'Borough':
        	continue
        #using 35 because it is close to the median age for all records
        ct2010  = list_line[3].strip()
        under35 = reduce(lambda x,y: x + int(y.replace(",","")),list_line[5:12],0)# agregate all under 35
        over35  = reduce(lambda x,y: x + int(y.replace(",","")),list_line[12:19],0)# agregate all over 35
        yield (ct2010,(under35,over35))

#this just in case the ct2010 is really not unique
def aggregateByct2010(v1,v2):
    return (v1[0] + v2[0], v2[1] + v2[1])


def ct2010noiseMapper(record):
    list_record = record.split(',')
    return (list_record[0].strip('u').strip("'").encode('utf-8'), int(list_record[1].strip()))


if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    ct2010_rdd       = sc.textFile(sys.argv[1])#rdd for the records coming from the 2010 census csv
    ct2010noise_rdd  = sc.textFile(sys.argv[2])#rdd for the no. complaints,ct2010 csv

    output = ct2010_rdd.mapPartitions(ct2010Mapper).reduceByKey(aggregateByct2010).\
                       join(ct2010noise_rdd.map(ct2010noiseMapper)).map(lambda x: (x[1][0], x[1][1]))


    output.saveAsTextFile(sys.argv[-1])
