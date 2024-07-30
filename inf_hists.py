import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
mpl.rcParams['figure.dpi'] = 300 
from matplotlib.lines import Line2D 
from matplotlib.patches import Patch

plt.style.use("/Users/oliveratkinson/Dropbox/cascade_interference/panos_plots/mystyle.mplstyle")
plt.rcParams.update({'figure.max_open_warning': 0})

#Randomly choosing 10 data points to plot and then fixing
#print(sorted(list(np.random.randint(1, 201, 15))))
file_ids = [16, 17, 50, 59, 62, 75, 95, 97, 106, 113, 132, 145, 151, 172, 185]

#Getting the full list of m_H3, signals and signals + inf.
m_H3s, m_H2s, h3_tt_s, h3_tt_si, h2_tt_s, h2_tt_si, h2_h1h1_s, h2_h1h1_si = [], [], [], [], [], [], [], []
mass_dat = open("/Users/oliveratkinson/Dropbox/cascade_interference/model/singlet_high_full.dat", "r")
for line in mass_dat: 
    m_H3s.append(line.split()[0])
    m_H2s.append(line.split()[1])

"""
inf_data = open("/Users/oliveratkinson/Dropbox/cascade_interference/model/analyse/interference_data.dat", "r")
for line in inf_data:
    h3_tt_s.append(line.split()[2])
    h3_tt_si.append(line.split()[3])
    h2_tt_s.append(line.split()[4])
    h2_tt_si.append(line.split()[5])
    h2_h1h1_s.append(line.split()[10])
    h2_h1h1_si.append(line.split()[11])
"""

#Opening the files and getting the relevant data for signal-interefernce plots
def dat_plot(num, chan):    
    sig_data = open("/Users/oliveratkinson/Documents/PhD/Research/inf_data/"+chan+"/m_signal_"+str(num)+".dat", "r")
    ms, sigs, sigs_inf = [], [], []
    for line in sig_data: 
        ms.append(line.split()[0])
        sigs.append(line.split()[1])

    inf_data = open("/Users/oliveratkinson/Documents/PhD/Research/inf_data/"+chan+"/m_signal_inf_"+str(num)+".dat", "r")
    for line in inf_data: 
        sigs_inf.append(line.split()[1])

    #Converting to numbers rather than strings
    sigs = [float(sig) for sig in sigs]
    ms = [float(m) for m in ms]
    sigs_inf = [float(sig_inf) for sig_inf in sigs_inf]

    #Only interested in certain mass ranges based on the decaying higgs; 300ish < m < 850ish for h3, 300ish < m < 700ish for h2
    #Also including details for the plotting
    if int(chan[-1]) == 3:
        m = round(float(m_H3s[num-1]), 2)
        cut_l, cut_h = ms.index(335), ms.index(855)
        title = r"$m_{H_3}=\;$"+str(m)+r' GeV'
        if chan[1] == "1":
            xlab, ylab = r'$m_{H_3}$ [GeV]', r'$\frac{d\sigma}{dm_{H_1H_1}}$ [fb/GeV]'
        elif chan[1] == "2":
            xlab, ylab = r'$m_{H_3}$ [GeV]', r'$\frac{d\sigma}{dm_{H_2H_1}}$ [fb/GeV]'
        else:
            xlab, ylab = r'$m_{H_3}$ [GeV]', r'$\frac{d\sigma}{dm_{tt}}$ [fb/GeV]'
    elif int(chan[-1]) == 2:
        m = round(float(m_H2s[num-1]), 2)
        cut_l, cut_h = ms.index(305), ms.index(655)
        title = r"$m_{H_2}=\;$"+str(m)+r' GeV'
        if chan[0] == "t":
            xlab, ylab = r'$m_{H_2}$ [GeV]', r'$\frac{d\sigma}{dm_{tt}}$ [fb/GeV]'
        elif chan[0] == "h":
            xlab, ylab = r'$m_{H_2}$ [GeV]', r'$\frac{d\sigma}{dm_{h_1h_1}}$ [fb/GeV]'

    ms, sigs, sigs_inf = ms[cut_l:cut_h], sigs[cut_l:cut_h], sigs_inf[cut_l:cut_h]

    plt.figure()
    plt.bar(ms, sigs, width=10, color='#348ABD', label="Signal")
    plt.step(ms, sigs_inf, where='mid', color='#E24A33', label='Inf. + Signal')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend(loc="upper right")
    #plt.title(title)
    plt.savefig("inf_plots/"+chan+"/"+chan+"_"+str(num)+".pdf", bbox_inches='tight')


#Doing the plots of the various channels
#for i in file_ids:
    #dat_plot(i, "tt_h3")
    #dat_plot(i, "h2h1_h3")
    #dat_plot(i, "h1h1_h3")
    #dat_plot(i, "tt_h2")
    #dat_plot(i, "h1h1_h2")
dat_plot(1287, "tt_h3")
"""
sigs_plot_tt_h3, sigs_rat_tt_h3, sigs_plot_tt_h2, sigs_rat_tt_h2, sigs_rat_h1h1_h2, sigs_plot_h1h1_h2 = [], [], [], [], [], []
for i in file_ids:
    sigs_plot_tt_h3.append(float(h3_tt_s[i]))
    sig_rat_tt_h3 = float(h3_tt_si[i]) / float(h3_tt_s[i])
    sigs_rat_tt_h3.append(sig_rat_tt_h3) 

    sigs_plot_tt_h2.append(float(h2_tt_s[i]))
    sig_rat_tt_h2 = float(h2_tt_si[i]) / float(h2_tt_s[i])
    sigs_rat_tt_h2.append(sig_rat_tt_h2) 

    sigs_plot_h1h1_h2.append(float(h2_h1h1_s[i]))
    sig_rat_h1h1_h2 = float(h2_h1h1_si[i]) / float(h2_h1h1_s[i])
    sigs_rat_h1h1_h2.append(sig_rat_h1h1_h2) 


plt.figure()
plt.tight_layout()
plt.scatter(sigs_plot_tt_h3, sigs_rat_tt_h3)
plt.xlabel("Signal "r'$\sigma$ (fb)')
plt.ylabel("(Signal + Inf.) / Signal")
plt.savefig("inf_plots/tt_h3/tt_h3_sig_inf.png")

plt.figure()
plt.tight_layout()
plt.scatter(sigs_plot_tt_h2, sigs_rat_tt_h2)
plt.xlabel("Signal "r'$\sigma$ (fb)')
plt.ylabel("(Signal + Inf.) / Signal")
plt.savefig("inf_plots/tt_h2/tt_h2_sig_inf.png")

plt.figure()
plt.tight_layout()
plt.scatter(sigs_plot_h1h1_h2, sigs_rat_h1h1_h2)
plt.xlabel("Signal "r'$\sigma$ (fb)')
plt.ylabel("(Signal + Inf.) / Signal")
plt.savefig("inf_plots/h1h1_h2/h1h1_h2_sig_inf.png")
#plt.show()
"""
