import sys
import pyspark
import operator
import csv
import itertools

#**************** BEGINING OF AUXILIARY CODE *********************************
###############################################################################
##
## Copyright (C) 2016, The City College of New York (CCNY).
## All rights reserved.
## Contact: hvo@@cs.ccny.cuny.edu
##
## This file is part of the Big Data Management & Analysis class, CUSP-GX-5008.
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are met:
##
##  - Redistributions of source code must retain the above copyright notice,
##    this list of conditions and the following disclaimer.
##  - Redistributions in binary form must reproduce the above copyright
##    notice, this list of conditions and the following disclaimer in the
##    documentation and/or other materials provided with the distribution.
##  - Neither the name of NYU-Poly nor the names of its
##    contributors may be used to endorse or promote products derived from
##    this software without specific prior written permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
## AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
## THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
## PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
## CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
## EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
## PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
## OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
## WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
## OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
## ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
###############################################################################


def csvRDD(rdd, hasHeader=True):
    self = CSVParser()
    self.hasHeader = hasHeader
    self.header = rdd.first()
    self.fields = csv.reader([self.header]).next()
    if not self.hasHeader:
        self.header = None
    cachedRdd = rdd.cache()
    rdd1 = rdd.mapPartitionsWithIndex(self.parseCompleteRecords)
    rdd2 = rdd.mapPartitions(self.parsePartialRecords) \
        .coalesce(1) \
        .mapPartitionsWithIndex(self.parseCompleteRecords)
    return rdd1.union(rdd2)

class CSVParser():
    def __init__(self):
        pass

    def parseCompleteRecords(self, index, lines):
        if self.hasHeader and index==0:
            peek = lines.next()
            if peek!=self.header:
                lines = itertools.chain([peek], lines)
        fieldCount = len(self.fields)
        reader = csv.reader(lines, strict=True)
        try:
            for row in reader:
                if len(row)==fieldCount:
                    yield row
        except:
            pass

    def parsePartialRecords(self, lines):
        (fieldCount, fullStart, fullEnd, line_num) = (len(self.fields), 0, 0, 0)
        (l1, l2) = itertools.tee(lines, 2)
        reader = csv.reader(l1, strict=True)
        try:
            for row in reader:
                steps = reader.line_num-fullEnd
                if len(row)!=fieldCount:
                    fullStart = reader.line_num
                    for line in itertools.islice(l2, steps):
                        yield line
                else:
                    next(itertools.islice(l2, steps, steps), None)
                fullEnd = reader.line_num
        except:
            for line in itertools.islice(l2, reader.line_num-fullEnd):
                yield line

#**************** END OF AUXILIARY CODE *********************************
###############################################################################

def filter_construction(record):
    if "Construction" in record[2] or "construction" in record[2]:
        return record

def construction_per_day(record):
    return record[1].strip().split(" ")[0].split("'")[1], 1

if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    noise_data = sc.textFile(','.join(sys.argv[1:-1]), use_unicode=False).cache()
    rdd = csvRDD(noise_data)
    construction_count = rdd.filter(lambda s: filter_construction(s)).map(lambda s: construction_per_day(s)).reduceByKey(operator.add)
    construction_count.saveAsTextFile(sys.argv[-1])
