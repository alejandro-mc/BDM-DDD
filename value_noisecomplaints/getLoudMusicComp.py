import pyspark
import operator
import sys

#311 call 2010 to present csv

#0  Unique Key,Created Date,Closed Date,Agency,Agency Name,
#5  Complaint Type,Descriptor,Location Type,Incident Zip,Incident Address,
#10 Street Name,Cross Street 1,Cross Street 2,Intersection Street 1,
#14 Intersection Street 2,Address Type,City,Landmark,Facility Type,Status,
#20 Due Date,Resolution Description,Resolution Action Updated Date,
#23 Community Board,Borough,X Coordinate (State Plane),Y Coordinate (State Plane),
#27 Park Facility Name,Park Borough,School Name,School Number,School Region,
#32 School Code,School Phone Number,School Address,School City,School State,
#37 School Zip,School Not Found,School or Citywide Complaint,Vehicle Type,
#41 Taxi Company Borough,Taxi Pick Up Location,Bridge Highway Name,
#44 Bridge Highway Direction,Road Ramp,Bridge Highway Segment,Garage Lot Name,
#48 Ferry Direction,Ferry Terminal Name,Latitude,Longitude,Location




def mapToLots(records):
    import rtree
    import csv
    import os
    os.chmod('plutoindex.idx',0777)
    os.chmod('plutoindex.dat',0777)
    file_index = rtree.index.Rtree('plutoindex')
    for record in records:
        list_record=[]
        for line in csv.reader([record.encode('utf-8')]):
            list_record = line
        if len(list_record) < 27:
           continue
        compType   = list_record[5].upper()
        descriptor = list_record[6].upper()
        if compType.count('NOISE') < 1 or descriptor.count('LOUD MUSIC/PARTY') < 1:
           continue
        xcoord = list_record[25].strip()
        ycoord = list_record[26].strip()
        if all((xcoord,ycoord)):
           #check intersection
           xcoord = int(xcoord)
           ycoord = int(ycoord)
           for lot in file_index.intersection((xcoord,ycoord),objects = True):
               yield (lot.object,1)  
           

def mapResUnits(pairs):
    import pickle
    
    with open('plutodict','rb') as fi:
         pluto_dict = pickle.load(fi)

    for pair in pairs:
        dict_entry = pluto_dict[pair[0]]
        property_value = dict_entry[1]
        res_units      = dict_entry[0]
        if res_units < 1:
           continue

        yield (property_value, pair[1] / float(res_units))#pair[1] = number of noise complaints


if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    calls311  = sc.textFile(sys.argv[1])

    output    = calls311.mapPartitions(mapToLots).reduceByKey(operator.add).\
                mapPartitions(mapResUnits)
        
    
    output.saveAsTextFile(sys.argv[-1])
