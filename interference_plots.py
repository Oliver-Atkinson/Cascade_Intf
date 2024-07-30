import numpy as np
import matplotlib.pyplot as plt

#Opening the file and getting the relevant data for h3 -> tt signal-interefernce plots
full_data = open("/Users/oliveratkinson/Dropbox/cascade_interference/model/analyse/interference_data.dat", "r")
sigs, sigs_inf = [], []
for line in full_data: 
    sigs.append(line.split()[10])
    sigs_inf.append(line.split()[11])

#Converting to numbers rather than strings
sigs, sigs_inf = sigs[1:], sigs_inf[1:]
sigs = [float(sig) for sig in sigs]
sigs_inf = [float(sig_inf) for sig_inf in sigs_inf]

sigs_rat = []
print(len(sigs))

for i in range(len(sigs)):
    sig_rat = sigs_inf[i] /sigs[i]
    #print(sig_rat)
    sigs_rat.append(sig_rat)

plt.figure()
plt.scatter(sigs, sigs_rat)
plt.xlabel("Signal")
plt.ylabel("(Signal + Inf.) / Signal")
plt.savefig("H2_H1H1_sig_inf.png")
plt.show()

