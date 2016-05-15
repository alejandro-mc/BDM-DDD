##Imports
import pyspark
import rtree
import geopandas as gpd
import shapely.geometry as geom
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



import operator
import heapq

def callMapper(calls):
    import rtree
    import geopandas as gpd
    import shapely.geometry as geom
    import csv
    import fiona.crs
    #first create index
    index = rtree.Rtree()
    #get geometry from geojson in NY stateplane projection coordinates
    ctracts2010 = gpd.read_file('2010CensusTracts.geojson').to_crs(fiona.crs.from_epsg(2263))
    
    #index geometry
    for idx,geometry in enumerate(ctracts2010.geometry):
        index.insert(idx,geometry.bounds)

    #for each 311 call record yield (ct2010, 1)
    ct2010 = 0
    for call in calls:
        for line in csv.reader([call.encode('utf-8')]):
            list_call = line
        if  call != '' and list_call[0] != 'Unique Key':#check for empty row and header
            
            if not all((list_call[25].strip(),list_call[26].strip())):
               continue

            callx = float(list_call[25])#callx is the x coordinate NY (state plane) projection
            cally = float(list_call[26])#cally  ...   y    ....

            call_location = geom.Point(callx,cally)

            #get call ct2010
            matches = list(index.intersection((call_location.x,call_location.y)))
            for ind in matches:
                if any(map(lambda x: x.contains(call_location), ctracts2010.geometry[ind])):
                    ct2010 = ctracts2010.ct2010[ind]

            yield (ct2010, 1)


if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    calls = sc.textFile(','.join(sys.argv[1:-1]))

    output = calls.mapPartitions(callMapper).reduceByKey(operator.add)


    output.saveAsTextFile(sys.argv[-1])
