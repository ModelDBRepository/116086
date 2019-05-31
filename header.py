

############################
#       parameters         #
############################

vmFile      = 'vm_sta.txt'  # file containing the voltage STA

dt          = 0.048         # time step in ms
t_cut       = 1.0           # time cut before spike in ms
n_cut       = int(t_cut/dt) 
n_smooth    = 0             # SD for smoothing in timesteps

Iext    = -0.2              # DC in nA
ge      = 0.032             # mean exc. cond. in uS
gi      = 0.096             # mean inh. cond. in uS
se      = 0.012             # exc. cond. fluctuations in uS
si      = 0.0072            # inh. cond. fluctuations in uS
gl      = 0.015             # leak cond. in uS
vl      = -92.66            # leak reversal potential in mV
cap     = 0.26              # capacitance in nF
te      = 2.728             # exc. correlation time in ms
ti      = 10.49             # inh. correlation time in ms
ve      = 0.                # exc. reversal potential in mV
vi      = -75.              # inh. reversal potential in mV
