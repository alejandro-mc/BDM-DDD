from rtree import index
import csv
import sys

##pluto csv file header

#0  Borough,Block,Lot,CD,CT2010,CB2010,SchoolDist,Council,ZipCode,FireComp,
#10 PolicePrct,HealthArea,SanitBoro,SanitDistrict,SanitSub,Address,
#16 ZoneDist1,ZoneDist2,ZoneDist3,ZoneDist4,Overlay1,Overlay2,SPDist1,
#23 SPDist2,LtdHeight,AllZoning1,AllZoning2,SplitZone,BldgClass,LandUse,
#30 Easements,OwnerType,OwnerName,LotArea,BldgArea,ComArea,ResArea,OfficeArea,
#38 RetailArea,GarageArea,StrgeArea,FactryArea,OtherArea,AreaSource,
#44 NumBldgs,NumFloors,UnitsRes,UnitsTotal,LotFront,LotDepth,BldgFront,
#51 BldgDepth,Ext,ProxCode,IrrLotCode,LotType,BsmtCode,AssessLand,AssessTot,
#59 ExemptLand,ExemptTot,YearBuilt,BuiltCode,YearAlter1,YearAlter2,HistDist,
#66 Landmark,BuiltFAR,ResidFAR,CommFAR,FacilFAR,BoroCode,BBL,CondoNo,
#74 Tract2010,XCoord,YCoord,ZoneMap,ZMCode,Sanborn,TaxMap,
#81 EDesigNum,APPBBL,APPDate,PLUTOMapID,Version


def main():
  
    plutofile = open(sys.argv[1],'r')
    file_index = index.Rtree(sys.argv[2])
    id=0
    for line in plutofile:
        lot = csv.reader([line])
        for lst in lot:
            lot = lst
        if len(lot) < 77:
           continue
        if lot[0] =='Borough':
           continue
        if all((lot[1].strip(),lot[2].strip(),lot[75].strip(),lot[76].strip())):
           block_number = int(lot[1].strip())
           lot_number   = int(lot[2].strip())
           xcoord       = int(lot[75].strip())
           ycoord       = int(lot[76].strip())
           #create bounding box of 200 feet rad around the lot
           left         = xcoord - 200
           right        = xcoord + 200
           bottom       = ycoord - 200
           top          = ycoord + 200
           file_index.insert(id,(left,bottom,right,top),obj = (block_number,lot_number))
           id += 1


if __name__ == '__main__':
   if len(sys.argv) < 3:
      print "Usage <plutofile.csv> <rtree file name>"
      sys.exit(-1)

   main()
   
   
