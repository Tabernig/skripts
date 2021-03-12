import math
import sys
import os

os.chdir("D:\\temp")


with open("150709_121106_POLAR.txt", 'r') as inp, open('XYZKoordinaten.txt', 'w') as outp:
    for line in inp:
        linetemp = line.split(",")
        #print(linetemp)
        #print("phi:=",linetemp[0])
        x = (float(linetemp[2]))*math.cos((float(linetemp[0]))/180*math.pi)*math.sin((float(linetemp[1]))/180*math.pi)
        y = (float(linetemp[2]))*math.sin((float(linetemp[0]))/180*math.pi)*math.sin((float(linetemp[1]))/180*math.pi)
        z = (float(linetemp[2]))*math.cos((float(linetemp[1]))/180*math.pi)
        #print ("X:",x,"Y:",y,"Z:",z)
        x = str(x)
        outp.write(x)
        outp.write(",")
        y = str(y)
        outp.write(y)
        outp.write(",")
        z = str(z)
        outp.write(z)
        outp.write("\n")

print("Done")