
import os

os.chdir(r"C:/Users/ronny/Desktop/Tools/convert/Multiline_2_Oneline")

input = open("multiline_Input.txt")
output = open("oneline_Output.txt","w")

oneliner = ""
for line in input:
    line1 = line.strip("\n")
    line2 = line1.split(" ")
    for word in line2:
        oneliner += word+" "

output.write(oneliner)

input.close()
output.close()
print("Conversion done ...")