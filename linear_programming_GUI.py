# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:53:20 2020

@author: Emanuel
"""

# Define a function to create the desired plot.
import matplotlib.pyplot as plt
import numpy as np

def make_plot(event=None):
    # Get these variables from outside the function, and update them.
    global gasoline_percentage_1, gasoline_percentage_2
    global lpg_percentage_1, lpg_percentage_2
    global other_percentage_1, other_percentage_2
    global max_gas, max_lpg, max_other
    
    try:
        
    # Convert StringVar data to numerical data.
    gp1 = gasoline_percentage_1.get()
    gp2 = gasoline_percentage_2.get()
    lp1 = lpg_percentage_1.get()
    lp2 = lpg_percentage_2.get()
    op1 = other_percentage_1.get()
    op2 = other_percentage_2.get()
    mg = max_gas.get()
    ml = max_lpg.get()
    mo = max_other.get()
 #  phi = float(deltaPhi.get())

    
    #Range of the Plot
    x=np.arange(0,1000)
    x1=np.arange(0,1000)
    x2=np.arange(0,1000)
    
    y=(mg-(gp1*x))/gp2
    
    j=1
    for i in y:
        j+=1
        print(i,j)
        if i==0:
            break
    x=np.arange(0,j)
    y=(mg-(gp1*x))/gp2
    
    y1=(ml-(lp1*x1))/lp2
    
    j1=1
    for i1 in y1:
        j1+=1
        print(i1,j1)
        if i1==0:
            break
    x1=np.arange(0,j1)
    y1=(ml-(lp1*x1))/lp2
        
    y2=(mo-(op1*x2))/op2
    

    j2=1
    for i2 in y2:
        j2+=1
        print(i2,j2)
        if i2==0:
            break
    x2=np.arange(0,j2)
    y2=(mo-(op1*x2))/op2


    # Create the plot.
    plt.figure()
    plt.plot(x,y,"green")
    plt.plot(x1,y1,"blue")
    plt.plot(x2,y2,"red")
    plt.title("Linear Optmiization")
    plt.xlabel("Volume Phase 1 - 1,000 Barrels")
    plt.ylabel("Volume Phase 2 - 1,000 Barrels")
    plt.legend(('Gasoline', 'LPG', 'Other'),
               loc='upper center', shadow=True)
    plt.show()
    except:
        pass