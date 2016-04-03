#uploadtoCDB.py
#Written By: Alejandro Morejon Cortina (Apr 2016)
#usage:python uploadtoCDB.py <username> <filecontainingkey.txt> <upload.csv>

import sys
import requests
import csv
import json
import time

#sys.argv[1] is the your cartodb user name
#sys.argv[2] is the text file containing your api key
#sys.argv[3] is the csv file to be uploaded
if __name__ == "__main__":

   with open(sys.argv[2],'r') as fi: 
        key = fi.readline().strip('\n')

   cdbusername = sys.argv[1]

   #import url to cartodb account
   importurl = "https://" + cdbusername +".cartodb.com/api/v1/imports/?api_key="+key
               

   f = open(sys.argv[3],"rb")
   #request to upload file to cartodb
   r = requests.post(importurl,files={'file': f})
   
   print r.text

   f.close()

   response = json.loads(r.text)
   
   
   checkimporturl = "https://"+ cdbusername +".cartodb.com/api/v1/imports/" 
   status = requests.get(checkimporturl + response["item_queue_id"] + "?api_key=" + key)

   #wait for upload to finish
   while not json.loads(status.text)["state"] in ["complete","failure"]: 
         status = requests.get(checkimporturl + response["item_queue_id"] + "?api_key=" + key)
         time.sleep(1)

   

