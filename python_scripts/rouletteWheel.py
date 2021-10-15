#------------------------------------------------------------#
#                                                            #
#                    rouletteWheel.py                        #
#                                                            #
# rouletteWheel.py simulates a casino roulette wheel using   #
# python's internal random number generator.                 #
#                                                            #
# Input(s):                                                  #
#                                                            #
# Output(s):                                                 #
#                   Number the wheel lands on                #
#                                                            #
# Author  : Jack Rossetti                                    #
# Date    : 21-10-04                                         #
# Contact : jsrossetti23@gmail.com                           #
#                                                            #
#------------------------------------------------------------#
import random

print("Roulette Wheel Simulator!");

wheelType = 1;

if(wheelType == 1):
## begin if
    wheelSeq = ['0','28','9','26','30','11','7','20','32','17','5','22','34','15','3','24','36','13','1','00','27','10','25','29','12','8','19','31','18','6','21','33','16','4','23','35','14','2'];
## end if

#
# Define the probability of the ball landing in a pocket:
#
p = 1/len(wheelSeq);

#
# Define count array
#
count = [];

for i in range(0,len(wheelSeq)):
## begin for i
    count.append(0);
## end for i

N = 100000; # Number of spins

for ispin in range(0,N):
## begin for ispin
    #
    # Choose a random number in the range [0,1)
    #
    R = random.random();
    
    #
    # Determine the pocket in which the ball ends up in
    #
    for i in range(0,len(wheelSeq)):
    ## begin for i
        check = (i+1)*p;
        if(check > R):
        ## begin if
            print("Pocket Landed = %s, prob = %8.4f, rand = %8.4f" % (wheelSeq[i], i*p, R));
            count[i] = count[i]+1/N;
            break;
        ## end if
    ## end for i
## end for ispin

print(count);
print(p);

exit();
