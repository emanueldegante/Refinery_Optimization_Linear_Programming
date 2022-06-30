# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:54:38 2020

@author: Emanuel
"""

import matplotlib.pyplot as plt
import numpy as np

#def linear_programming_plots(a,b,c,a1,b1,c1,a2,b2,c2):
    
#----------------------------------------------------- Gasoline
a=24
b=.8
c=.44

x=np.arange(0,1000)

y=(a-(b*x))/c

j=1
for i in y:
    j+=1
    print(i,j)
    if i==0:
        break
x=np.arange(0,j)
y=(a-(b*x))/c
#------------------------------------------------------ LPG
a1=2
b1=.05
c1=.1

x1=np.arange(0,1000)

y1=(a1-(b1*x1))/c1

j1=1
for i1 in y1:
    j1+=1
    print(i1,j1)
    if i1==0:
        break
x1=np.arange(0,j1)
y1=(a1-(b1*x1))/c1
#------------------------------------------------------Other
a2=6
b2=.1
c2=.36

x2=np.arange(0,1000)

y2=(a2-(b2*x2))/c2

j2=1
for i2 in y2:
    j2+=1
    print(i2,j2)
    if i2==0:
        break
x2=np.arange(0,j2)
y2=(a2-(b2*x2))/c2

#-----------------------------------------------------Profit

x3=np.arange(0,1000)
v1=7.6
v2=9.8

y3=((243-(v2*x3))/v1)

j3=1
for i3 in y3:
    j3+=1
    print(i3,j3)
    if (i3<=0):
        break
x3=np.arange(0,j3)
y3=((243-(v2*x3))/v1)


#------------------------------------------------------Plot
plt.plot(x,y,"blue")
plt.plot(x1,y1,"blue")
plt.plot(x2,y2,"blue")
plt.plot(x3,y3,"red")
plt.title("Linear Optmiization")
plt.xlabel("Volume Phase 1 - 1,000 Barrels")
plt.ylabel("Volume Phase 2 - 1,000 Barrels")
plt.legend(('Gasoline', 'LPG', 'Other','Profit'),
           loc='upper center', shadow=True)