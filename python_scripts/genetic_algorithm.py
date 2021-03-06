#------------------------------------------------------------#
#                                                            #
#                    genetic_algorithm.py                    #
#                                                            #
# genetic_algorithm.py performs evolutionary optimzation us- #
# ing genetic algorithm. It is a research code that uses var-#
# ious selection, crossover, and mutation methods to find    #
# the minimum of a given objective.                          #
#                                                            #
# Input(s):                                                  #
#                                                            #
# Output(s):                                                 #
#                   Minimum value                            #
#                                                            #
# Author  : Jack Rossetti                                    #
# Date    : 21-10-04                                         #
# Contact : jsrossetti23@gmail.com                           #
#                                                            #
#------------------------------------------------------------#
import random
import math
import matplotlib.pyplot as plt
import numpy as np

print("");
print("****************************************************************");
print("*                                                              *");
print("*                    genetic_algorithm.py                      *");
print("*                                                              *");
print("* genetic_algorithm.py performs evolutionary optimzation using *");
print("* a genetic algorithm. It is a research code that uses various *");
print("* selection, crossover, and mutation methods to find the mini- *");
print("* mum of a given objective.                                    *");
print("*                                                              *");
print("* Input(s):                                                    *");
print("*                                                              *");
print("* Output(s):                                                   *");
print("*                   Minimum value                              *");
print("*                                                              *");
print("* Author  : Jack Rossetti                                      *");
print("* Date    : 21-10-04                                           *");
print("* Contact : jsrossetti23@gmail.com                             *");
print("*                                                              *");
print("****************************************************************");
print("");

seed  = 19920123;
#random.seed(seed);

crossover = 0.85;
mutation  = 0.005;

Nsol  = 10000;
xmax  =  100.0;
xmin  = -100.0;
rng   = xmax-xmin;
offset= xmin/rng;
dx    = (xmax-xmin)/(Nsol-1)
xsol  = np.zeros([Nsol,1]);
fsol  = np.zeros([Nsol,1]);
for i in range(0, Nsol):
## begin for i
    xsol[i] = xmin+dx*i;
    fsol[i] = xsol[i]*xsol[i]#+1000*math.sin(15*math.pi*xsol[i]/rng);
## end for i
 
Ngene =  16;
Mpop  =  10;
Bmax  = 2.0**(Ngene)-1.0;
x     = np.zeros([Mpop,Ngene])
xbin  = np.zeros([Mpop,    1])
xind  = np.zeros([Mpop,    1])
find  = np.zeros([Mpop,    1])
nind  = np.zeros([Mpop,    1])

#
# Initialize population
#
for ipop in range(0,Mpop):
## begin for ipop
    xsum  = 0;
    for igene in range(1,Ngene+1):
    ## begin for igene
        ii         = Ngene-igene;
        x[ipop,ii] = random.randint(0,1);
    ## end for igene
## end for ipop

Niter = 250;

fig = plt.figure();
    
for k in range(0,Niter):
## begin for k
    fsum  = 0;
    for ipop in range(0,Mpop):
    ## begin for ipop
        xsum  = 0;
        for igene in range(1,Ngene+1):
        ## begin for igene
            ii         = Ngene-igene;
            xsum       = x[ipop,ii]*2**(igene-1) + xsum;
        ## end for igene
        xval       = ((xsum/Bmax)+offset)*rng;
        xbin[ipop] = xsum;
        xind[ipop] = xval;
        find[ipop] = xval*xval#+1000*math.sin(15*math.pi*xval/rng);
        fsum       = fsum + find[ipop];
    ## end for ipop
    
    for ipop in range(0,Mpop):
    ## begin for ipop
        nind[ipop] = 1-(find[ipop]/fsum);
    ## end for ipop

    if(k > 0):
        plt.clf();
        
    plt.plot(xsol, fsol);
    plt.plot(xind, find, 'ro');
    plt.draw();
    plt.pause(0.001);
    
    sort_find = np.argsort(find, axis=0);
    
    #
    # Determine the mating pool
    #
    xnew    = np.zeros([Mpop, Ngene]);
    
    for imate in range(0, int(Mpop/2)):
    ## begin for imate
        
        xparent = np.zeros([   2,Ngene]);
        
        for iparent in range(0,2):
        ## begin for ipop
            R    = random.random();
            rsum = 0;
            for jpop in range(0,Mpop):
            ## begin for jpop
                rsum = rsum + nind[sort_find[jpop]]
                if(rsum > R):
                ## begin if
                    xparent[iparent,:] = x[sort_find[jpop],:];
                    break;
                ## end if
            ## end for jpop
        ## end for ipop

        xchild= xparent;
        R = random.random();
        if(R < crossover):
        ## begin if
            cgene = random.randint(1,Ngene-1);
            for igene in range(cgene+1,Ngene+1):
            ## begin for igene
                ii = Ngene-igene
                xchild[0,ii] = xparent[1,ii];
                xchild[1,ii] = xparent[0,ii];
            ## end for igene
        ## end if

        for ichild in range(0,2):
        ## begin for ichild
            for igene in range(1,Ngene+1):
            ## begin for igene
                ii= Ngene-igene;
                R = random.random();
                if(R < mutation):
                ## begin if
                    if(xchild[ichild,ii] > 0):
                    ## begin if
                        xchild[ichild,ii] = 0;
                    elif(xchild[ichild,ii] < 1):
                        xchild[ichild,ii] = 1;
                    ## end if
                ## end if
            ## end for igene
        ## end for ichild

        xnew[2*imate  ,:] = xchild[0,:];
        xnew[2*imate+1,:] = xchild[1,:];
    
    ## end for imate

    x     = xnew;
    fstar = min(find);
    print("Iteration: %5d, favg = %8.4f, fmin = %10.4e" % (k, fsum/Mpop, fstar) );

## end for k

plt.show();

exit();
