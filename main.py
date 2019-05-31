
from header import *
from methods import *


file=open(vmFile,'r') 

vm=zeros(5000,Float)
vms=zeros(1,Float)

# load voltage STA from file
file.seek(0)
i=0 
for line in file:
    vm[i] = float(line)    
    i+=1 

file.close()

vm=resize(vm,(i-n_cut,))        # exclude prespike interval
vms=vm

if(n_smooth>0):                 # smooth vm if necessary
    vms=smooth(vm,n_smooth)
        
g=sta(vms)
saveCond(g)




