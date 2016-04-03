#!/usr/bin/env python
import sys, time

def mapper():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.split(',')
        if line[0].isdigit():
           #line[1]  : Created Date
           #line[5]  : Complaint Type
           #line[50] : Latitude
           #line[51] : Longitude
           yearcreated = line[1].split(' ')[0].split('/')[2]
           if 'NOISE' in line[5].upper() and '2015' == yearcreated:
               #check for non empty latitude and longitude
               if line[50] != '' and line[51] !='':
                  print '%s,%s' % (line[50],line[51])
        
        else:
           print 'Latitude,Longitude'

if __name__=='__main__':
    mapper()
