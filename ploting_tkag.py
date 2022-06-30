# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:54:31 2020

@author: Emanuel
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:09:30 2020

@author: Emanuel
"""

import tkinter as tk 
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

def make_plot(mg,gp1,gp2,ml,lp1,lp2,mo,op1,op2,v_1,v_2,tp):
    
    fig = Figure(figsize=(6, 5), dpi=70)
    window=tk.Tk()
    window.wm_title("Refinery Linear Optimization")
    canvas = FigureCanvasTkAgg(fig, master=window)  
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)     #To expand when needed
    
    
    ax = fig.add_subplot(111)
    
    #mg=12
    #gp1=.5
    #gp2=.7
    #ml=5
    #lp1=.25
    #lp2=.25
    #mo=3
    #op1=.25
    #op2=.05
    
    #Range of the Plot
    x=np.arange(0,1000)
    x1=np.arange(0,1000)
    x2=np.arange(0,1000)
#--------------------------------------------------------- Gasoline     
    y=(mg-(gp1*x))/gp2
    
    j=1
    for i in y:
        j+=1
        print(i,j)
        if (i<=0):
            break
    x=np.arange(0,j)
    y=(mg-(gp1*x))/gp2
#--------------------------------------------------------- LPG    
    y1= (ml-(lp1*x1))/lp2
    
    j1=1
    for i1 in y1:
        j1+=1
        print(i1,j1)
        if (i1<=0):
            break
    x1=np.arange(0,j1)
    y1=(ml-(lp1*x1))/lp2
#--------------------------------------------------------- Other        
    y2= (mo-(op1*x2))/op2
    
    
    j2=1
    for i2 in y2:
        j2+=1
        print(i2,j2)
        if (i2<=0):
            break
    x2=np.arange(0,j2)
    y2=(mo-(op1*x2))/op2

#------------------------------------------------------------Profit    
    x3=np.arange(0,1000)
    #v1=7.6
    #v2=9.8
    
    y3=((tp-(v_2*x3))/v_1)
    
    j3=1
    for i3 in y3:
        j3+=1
        print(i3,j3)
        if (i3<=0):
            break
    x3=np.arange(0,j3)
    y3=((tp-(v_2*x3))/v_1)
    
    ax.plot(x, y,"blue")
    ax.plot(x1,y1,"blue")
    ax.plot(x2,y2,"blue")
    ax.plot(x3,y3,'red')
    ax.legend('glop')
    ax.set_title('Linnear Programming')
    ax.set_ylabel("Volume Phase 1 - 1,000 Barrels")
    ax.set_xlabel("Volume Phase 2 - 1,000 Barrels")
    
    
    #=======================================================================Exit Button
    def exit():
        window.quit()     # stops mainloop
        window.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = tk.Button(master=window, text="Quit",command=exit, width=8, height=2, )
    button.pack(side=tk.BOTTOM)
    
    
    tk.mainloop()