import sys
import pyspark

from csv_parser import csvRDD

def filter_noise(record):
    if 'NOISE' in record[5].upper():
        return record

# record[0] = id, record[1] = time, record[6] = description, record[52] = (lat, long)
def reduce_data_size(record):
    return record[0],record[1], record[6], record[52]

if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    input_311_data = sc.textFile(','.join(sys.argv[1:-1]), use_unicode=False).cache()
    rdd_input = csvRDD(input_311_data)

    noise_data = rdd_input.filter(lambda r: filter_noise(r))

    reduced_data = noise_data.map((lambda s: reduce_data_size(s)))

    noise_data.saveAsTextFile(sys.argv[-1])
    #reduced_data.saveAsTextFile(sys.argv[-1]) # Comment out if want to execute this line vs the other