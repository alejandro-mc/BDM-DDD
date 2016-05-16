import pickle
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
    dict_blocklot_resunits = {}
    for line in plutofile:
        lot = csv.reader([line])
        for lst in lot:
            lot = lst
        if len(lot) < 59:
           continue
        if lot[0] =='Borough':
           continue
        if all((lot[1].strip(),lot[2].strip(),lot[46].strip(),lot[58].strip())):
           block_number = int(lot[1].strip())
           lot_number   = int(lot[2].strip())
           res_units    = int(lot[46].strip())
           prop_value   = int(lot[58].strip())
           dict_blocklot_resunits[(block_number,lot_number)] = (res_units,prop_value)

    #picle the dictionary
    with open(sys.argv[2],'wb') as out:
         pickle.dump(dict_blocklot_resunits,out,-1)


if __name__ == '__main__':
   if len(sys.argv) < 3:
      print "Usage <plutofile.csv> <picled dictionary name>"
      sys.exit(-1)

   main()
   
   
