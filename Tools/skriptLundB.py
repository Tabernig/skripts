#calc l und b

area = input("Flaeche eingeben:")
perimeter = input("Umfang eingeben:")

area1 = float(area)
perimeter1 = float(perimeter)

l = float(0)

while True:
    areacal = (perimeter1 * l - (2.0*l*l))/2.0
    if areacal < area1:
        l += float(0.005)
    if areacal >= area1:
        break


Bfin = area1/l

print("Breite = "+str(l)+" \nLaenge = "+str(Bfin))
print("Done")