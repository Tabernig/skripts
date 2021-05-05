import matplotlib.pyplot as plt 
import os
import math
import matplotlib


xLabel = "Jährlichkeit"


pfad = "D:\_Programmieren\data_for_script\\"
outName = "jahr"
filename = pfad+"jahre.txt"



with open(filename) as txtFile:
    lines = txtFile.readlines()
    #6lines
    count = 0
    titles = []
    QK_MAX = []
    tQK_MAX = []
    Kum_Fracht = []
    Kum_Regenmenge = []
    Dauer = []
    Jahr = []
    for i in range(len(lines)):
        if count == 0 or count % 6 == 0: #Add titles to list
            titles.append(lines[i])
        line = lines[count].split()
        #print(line)
        if line[0] == "QK-MAX":
            QK_MAX.append(line[1])
        if line[0] == "tQK-MAX":
            tQK_MAX.append(line[1])
        if line[0] == "Kum." and line[1] == "Fracht":
            Kum_Fracht.append(line[2])
        if line[0] == "Kum." and line[1] == "Regenmenge":
            Kum_Regenmenge.append(line[2])
        if line[0] == "Dauer":
            Dauer.append(line[1])
        if line[0] == "Simulationsergebnisse:":
            Jahr.append(line[1])
        
        count+=1
print(Jahr)
# #für neigungen
# neigung = []
# for value in Jahr:
#     #print(value)
#     newVal = str(round(math.degrees(math.atan(float(value))),2))+"°"
#     neigung.append(newVal)
#     #print(newVal)
# # #print(math.atan(57))

# print(titles)
# print(QK_MAX)
# # print(tQK_MAX)
# # print(Kum_Fracht)
# # print(Kum_Regenmenge)
# # print(Dauer)
# # print(Jahr)
# print(neigung)

fig = plt.figure()
gs = fig.add_gridspec(5, hspace=0.5)
axs = gs.subplots(sharex=True, sharey=False)
fig.suptitle('Vergleich der Simulationsergebnisse')

axs[0].plot(Jahr, QK_MAX, label = "QK_MAX_m³/s")
axs[1].plot(Jahr, tQK_MAX, label = "tQK_MAX_min")
axs[2].plot(Jahr, Kum_Fracht, label = "Kum_Fracht_m³")
axs[3].plot(Jahr, Kum_Regenmenge, label = "Kum_Regen_m³")
axs[4].plot(Jahr, Dauer, label = "Dauer_min")
#matplotlib.rc ("ytick",labelsize=5)
# Hide x labels and tick labels for all but bottom plot.
count = 0
for ax in axs:
    ax.legend(bbox_to_anchor=(1, 1), loc='center left', fontsize='xx-small')
    
    plt.setp(ax.get_yticklabels(), fontsize=5)
    plt.setp(ax.get_xticklabels(), fontsize=5) #change labelsize
    count += 1
#plt.show()
plt.xlabel(xLabel)
plot = plt.gcf()
plt.savefig(pfad+outName+".png", dpi = 300, bbox_inches="tight")


# plt.plot(neigung, Dauer, label = "Dauer_min")
# plt.plot(neigung, QK_MAX, label = "QK_MAX_m³/s")
# plt.plot(neigung, tQK_MAX, label = "tQK_MAX_min")
# plt.plot(neigung, Kum_Fracht, label = "Kum_Fracht_m³")
# plt.plot(neigung, Kum_Regenmenge, label = "Kum_Regen_m³")
# plt.xlabel(xLabel)
# plt.legend(bbox_to_anchor=(1, 1), loc='upper right', fontsize='xx-small')
# plt.title("Sensititvitätsstudie bei den einzelnen Simulationsergebniswerten")
# #plt.show()
# plt.gcf()
# plt.savefig(pfad+outName+".png", dpi = 300)


print("done")