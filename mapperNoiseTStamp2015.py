#!/usr/bin/env python
import sys, time

def to_timestamp(timestr):
    datestr,timestr,amstr = timestr.split(' ')
    month,day,year = datestr.split('/')
    hour,minutes,seconds = timestr.split(':')
    am = (amstr == 'AM')
    if am:
       if hour == '12':
          hour='00'
    else:
       if hour != '12':
          hour = str(int(hour) + 12)
    
    return '%s-%s-%s %s:%s:%s' % (year,month,day,hour,minutes,seconds)

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
                  print '%s,%s,%s' % (line[51],line[50],to_timestamp(line[1]))
        
        else:
           print 'Longitude,Latitude,Date_Created'

if __name__=='__main__':
    mapper()
