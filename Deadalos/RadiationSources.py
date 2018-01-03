
from Radiation import RadComp,Radiation,area
from Materials import Al_2024,Ti_1

f1,E1 = 10.**8,2.7*10.**(-18)
f2,E2 = 10.**10,4.19*10.**(-13)
f3,E3 = 10.**10.5,5.*10.**(-13)
f4,E4 = 10.**12,4.5*10.**(-15)
f5,E5 = 10.**12,8.*10.**(-16)
f6,E6 = 10.**12,10.**(-15)
f7,E7 = 10.**14,1.05*10.**(-12)
f8,E8 = 10.**14.5,10.**(-17)

rc1 = RadComp(f1,E1)
rc2 = RadComp(f2,E2)
rc3 = RadComp(f3,E3)
rc4 = RadComp(f4,E4)
rc5 = RadComp(f5,E5)
rc6 = RadComp(f6,E6)
rc7 = RadComp(f7,E7)
rc8 = RadComp(f8,E8)
rads = [rc1,rc2,rc3,rc4,rc5,rc6,rc7,rc8]

radiation = Radiation(rads)

print 75./(8.*7.*24*3600.)
E = 0.
mat = Ti_1
walls = [[[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]]]
walls2 = [[[0.5,mat],[0.5,mat],[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat],[2.,mat],[2.,mat]],\
         [[0.5,mat],[2.,mat],[2.,mat]],\
         [[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat],[0.5,mat],[0.5,mat]],\
         [[0.5,mat],[0.5,mat],[0.5,mat]],\
         [[0.5,mat]],\
         [[0.5,mat],[2.,mat],[2.5,mat]],\
         [[0.5,mat],[2.,mat],[2.5,mat]],\
         [[0.5,mat],[2.,mat],[2.5,mat]],\
         [[0.5,mat],[2.,mat],[2.5,mat]],\
         [[0.5,mat],[2.,mat],[2.5,mat]]]
for i in range(1,15):
    A = area(i,5.)
    E += radiation.energyRate(i,A,walls[i-1])
print E
    
    