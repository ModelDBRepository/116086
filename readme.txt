
###################################################################
#  STA analysis                                                   #
#                                                                 #
#  based on the publication                                       #
#                                                                 #
#  Martin Pospischil, Zuzanna Piwkowska, Michelle Rudolph,        #
#  Thierry Bal and Alain Destexhe "Calculating Event-Triggered    # 
#  Average Synaptic Conductances From the Membrane Potential",    #
#  J Neurophysiol 97:2544-2552, 2007.                             #
#                                                                 #
###################################################################

This application performs a conductance analysis of spike-triggered 
average voltage traces. A file containing this voltage STA is 
loaded, and a short adjustable interval before the spike is removed 
from the trace. If necessary, the voltage STA can be smoothed in 
order to minimise the effect of recording noise. All parameters are 
provided by the file 'header.py', the call 'python main.py' from 
the system prompt starts the analysis. The time courses of the 
excitatory and inhibitory STAs are then written to the files 
'ge_sta.txt' and 'gi_sta.txt', respectively. In order for this to 
work, the python scripting language along with the packages 
'Numeric' and 'pylab' need to be installed.

Modifications need only be done to the 'header.py'-file. The 
adjustable parameters contained therein are as follows:

vmFile      -   file containing the voltage STA in a single column
dt          -   time step (inverse of sampling frequency) in ms
t_cut       -   length of interval before spike in ms that is       
                removed from the analysis
n_smooth    -   SD in timesteps of the Gaussian filter that is used 
                for smoothing
Iext        -   current level in nA
ge          -   mean of exc. conductance distribution in uS
gi          -   mean of inh. conductance distribution in uS
se          -   standard deviation (SD) of exc. conductance 
                distribution in uS
si          -   SD of inh. conductance distribution in uS
gl          -   leak conductance in uS
vl          -   leak reversal potential in mV
cap         -   capacitance in nF
te          -   correlation time constant of excitation in ms
ti          -   correlation time constant of inhibition in ms
ve          -   reversal potential of excitation in mV
vi          -   reversal potential of inhibition in mV
