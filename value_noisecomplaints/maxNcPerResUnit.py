#script to very veryfy noise complaints per residential units

with open('propvalue_vs_noise_per_resunit.csv') as csvpairs:
     maximum =0
     for line in csvpairs:
         newvalue = float(line.encode('utf-8').split(',')[1].strip())
         maximum = max(maximum,newvalue)
     print maximum
