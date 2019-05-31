
from Numeric import *
from header import *
from pylab import *



def gauss_f(x, m, s):
    """returns a Gaussian of mean 'm' and standard deviation 's' at point 'x'"""
    return exp(-(x-m)**2/2./s**2)/sqrt(2.*pi*s**2)


def smooth(a, s):
    """smoothes the array 'a' with a Gaussian filter, whos standard deviation is 's' time steps"""
    sa = size(a)-6*s        # cut gaussian at +- 3*sigma
    r = zeros(sa, Float)
    g = array(arange(-3.*s,3.*s,1.))
    g = gauss_f(g, 0., s)
    norm=sum(g)
    for i in range(0, sa):
        r[i] = dot(a[i:6*s+i],g)/norm
             
    return r
        

def sta(vm):
    """computes the conductance STAs from the array 'vm' containing the voltage STA"""
    n=size(vm)
    tm = cap/gl         # memb. time constant in ms
# 
    vm0=vm[:n-1]  
    vmp=vm[1:n]  
    ge0 = ge            # g_e^0
    gi0 = gi            # g_i^0
# 
    dv = (vmp-vm0)/dt   # voltage derivative
    a = -(vm0-ve)/(vm0-vi)
    a0 = a[1:n-2]
    am = a[:n-3]
    b = -cap/(vm0-vi)*((vm0-vl)/tm+dv-Iext/cap)
    bp = b[2:n-1]
    b0 = b[1:n-2]
    bm = b[:n-3]
# 
    vec = zeros(n-1,Float)    
# 
    vec[1:n-2] = -2.*(dt**2*ge/se**2/te + a0/si**2/ti*(dt**2*gi+(bm+bp)* (ti**2-dt*ti)-b0*(dt**2-2.*dt*ti+2.*ti**2)))        
#         
    vec[0] = -2.*((dt**2*ge-dt*ge0*te+ge0*te**2)/se**2/te + a[0]/si**2/ti*(dt**2*gi+(b[1]+gi0)*(ti**2-dt*ti)-b[0]*(dt**2-2.*dt*ti+2.*ti**2)))
    vec[n-2] = -2.*(dt*ge/se**2 + a[n-2]/si**2*(dt*gi-b[n-2]*ti+b[n-3]*(ti-dt)))
#     
    sub_d = array([2.*((dt-te)/se**2+a[i-1]*a[i]/si**2*(dt-ti)) for i in range(1,n-1)])
# 
    dg = 2.*((dt**2-2.*dt*te+2.*te**2)/se**2/te+a**2/si**2/ti*(dt**2-2.*dt*ti+2.*ti**2))
    dg[n-2] = 2.*te/se**2 + 2.*a[n-2]**2*ti/si**2
#    
    # compose matrix 
    m = diag(dg,0)+diag(sub_d,-1)+diag(sub_d,1) 
#     m = diago(dg,0)+diago(sub_d,-1)+diago(sub_d,1) 
    m_inv = inverse(m)          # compute inverse
    tmpge = dot(m_inv,-vec)     # solve for excitation
    tmpgi = a*tmpge+b           # calculate inhibition
# 
    g=zeros((2,n,), Float)
    g[0,1:]=tmpge
    g[0,0] = ge0
    g[1,1:]=tmpgi
    g[1,0] = gi0
# 
    return g
        

        
def saveCond(g):
    """save conductance STAs to files"""
    ln = size(g[0])
    file=open('ge_sta.txt','w')
    for i in range(ln):
        file.write('%2.5f\n'%(g[0,i]))
        
    file.close()
#     
    file=open('gi_sta.txt','w')
    for i in range(ln):
         file.write('%2.5f\n'%(g[1,i]))
       
    file.close()
     
     
     