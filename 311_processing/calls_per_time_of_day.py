import sys
import pyspark
import operator

from csv_parser import csvRDD

def calls_per_time_of_day(records):
    for call in records:
        yield (call[1].split(" ")[1].strip(), 1)

if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    noise_data = sc.textFile(','.join(sys.argv[1:-1]), use_unicode=False).cache()
    rdd_input = csvRDD(noise_data)

    calls_per_day = rdd_input.mapPartitions(calls_per_time_of_day).reduceByKey(operator.add)

    calls_per_day.saveAsTextFile(sys.argv[-1])


