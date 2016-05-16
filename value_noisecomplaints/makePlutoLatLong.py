import pickle
import csv
import sys
import pyproj

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
    dict_blocklot_resunits = {}
    proj = pyproj.Proj(init="epsg:2263", preserve_units=True)
    for line in plutofile:
        lot = csv.reader([line])
        for lst in lot:
            lot = lst
        if len(lot) < 59:
           continue
        if lot[0] =='Borough':
           continue
        
        block_number = lot[1 ].strip()
        lot_number   = lot[2 ].strip()
        res_units    = lot[46].strip()
        prop_value   = lot[58].strip()
        xcoord       = lot[75].strip()
        ycoord       = lot[76].strip()

        if all((block_number,lot_number,res_units,prop_value,xcoord,ycoord)):
           block_number = int(block_number)
           lot_number   = int(lot_number)
           res_units    = int(res_units)
           prop_value   = int(prop_value)
           xcoord       = float(xcoord)
           ycoord       = float(ycoord)
           longlat      = proj(xcoord,ycoord,inverse=True) 
           dict_blocklot_resunits[(block_number,lot_number)] = (res_units,prop_value,longlat[0],longlat[1])

    #picle the dictionary
    with open(sys.argv[2],'wb') as out:
         pickle.dump(dict_blocklot_resunits,out,-1)


if __name__ == '__main__':
   if len(sys.argv) < 3:
      print "Usage <plutofile.csv> <picled dictionary name>"
      sys.exit(-1)

   main()
   
   
