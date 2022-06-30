# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:01:21 2020

@author: Emanuel
"""

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import ploting_tkag

#Global Variables
price_crude_1= None
price_crude_2= None
price_gasoline= None
price_lpg= None
price_other=None
phase_crude_1 = None
phase_crude_2 = None
phase_capacity_1= None
phase_capacity_2= None

gasoline_percentage_1=None
gasoline_percentage_2=None

lpg_percentage_1= None
lpg_percentage_2= None
proccessing_cost_1= None
proccessing_cost_2= None
other_percentage_1= None
other_percentage_2=None
operational_time_1=None
operational_time_2=None

calc_gas_1=None

max_gas=None
max_lpg=None
max_other=None

# This function is called whenever the button is pressed
def calculate():
    global price_crude_1
    global price_crude_2
    global price_gasoline
    global price_lpg
    global price_other
    global phase_crude_1
    global phase_crude_2
    global gasoline_percentage_1
    global gasoline_percentage_2
    global lpg_percentage_1
    global lpg_percentage_2
    global proccessing_cost_1
    global proccessing_cost_2
    global other_percentage_1
    global other_percentage_2
    global calc_gas_1
    global phase_capacity_1
    global phase_capacity_2

#Calculations
    try:

#--------------------------------------------------------------------------Amount Produced
        pc1 = phase_capacity_1.get()        #Phase 1
        gp1 = gasoline_percentage_1.get()
        ot1 = operational_time_1.get()
        calc_gas_1.set((pc1*gp1)/(ot1/24))  #Calc Amount Gas # 1

        lp1= lpg_percentage_1.get()        
        calc_lpg_1.set((pc1*lp1)/(ot1/24))  #Calc Amount lpg # 1

        op1=other_percentage_1.get()
        calc_other_1.set((pc1*op1)/(ot1/24)) #Calc Amount other # 1
   
        pc2 = phase_capacity_2.get()         #Phase 2
        gp2 = gasoline_percentage_2.get()
        ot2 = operational_time_2.get()
        calc_gas_2.set((pc2*gp2)/(ot2/24))  #Calc Amount Gas # 2
        
        lp2= lpg_percentage_2.get()
        calc_lpg_2.set((pc2*lp2)/(ot2/24))  #Calc Amount lpg # 2
        
        op2=other_percentage_2.get()
        calc_other_2.set((pc2*op2)/(ot2/24)) #Calc Amount other # 2
 #--------------------------------------------------------------------------Income       
        cg1=calc_gas_1.get()               # Income Gas 1
        pg=price_gasoline.get()
        income_gas_1.set((cg1*pg))
        
        cg2=calc_gas_2.get()               # Income Gas 2
        pg=price_gasoline.get()
        income_gas_2.set((cg2*pg))
        
        cl1=calc_lpg_1.get()               # Income lpg 1
        pl=price_lpg.get()
        income_lpg_1.set((cl1*pl))
        
        cl2=calc_lpg_2.get()               # Income lpg 2
        pl=price_lpg.get()
        income_lpg_2.set((cl2*pl))
        
        co1=calc_other_1.get()             # Income other 1
        po=price_other.get()
        income_other_1.set((co1*po))
        
        co2=calc_other_2.get()             # Income other 2
        po=price_other.get()
        income_other_2.set((co2*po))
        
        ig1=income_gas_1.get()             # Sum Income 1
        il1=income_lpg_1.get()
        io1=income_other_1.get()
        total_income_1.set(ig1+il1+io1)
        
        ig2=income_gas_2.get()             # Sum Income 2
        il2=income_lpg_2.get()
        io2=income_other_2.get()
        total_income_2.set(ig2+il2+io2)
        
        prc1=proccessing_cost_1.get()       #Total Production Cost 1
        total_production_1.set(prc1 * pc1)
        
        prc2=proccessing_cost_2.get()       #Total Production Cost 2
        total_production_2.set(prc2 * pc2)
        
        pcr1=price_crude_1.get()
        crude_cost_1.set((pcr1*pc1))       # Total Raw crude # 1 
        
        pcr2=price_crude_2.get()
        crude_cost_2.set((pcr2*pc2))       # Total Raw Crude # 2
        
        ti1=total_income_1.get()           # Total Profit # 1
        tp1=total_production_1.get()
        cc1=crude_cost_1.get()
        profit_1.set(ti1-tp1-cc1)
        
        ti2=total_income_2.get()           # Total Profit # 2
        tp2=total_production_2.get()
        cc2=crude_cost_2.get()
        profit_2.set(ti2-tp2-cc2)
        
        total_income.set(ti1+ti2)         #Total Income
        ti=total_income.get()
        
        total_production.set(tp1+tp2)     #Total Production Cost
        tp=total_production.get()
        
        total_crude_cost.set((cc1+cc2))   #Total Crude Cost
        tcc=total_crude_cost.get()
        
        total_profit.set(ti-tp-tcc)       # Total Profit
        
        v_1.set((gp1*pg)+(lp1*pl)+(op1*po)-(pcr1+prc1))      #Profit Function V1

        
        v_2.set((gp2*pg)+(lp2*pl)+(op2*po)-(pcr2+prc2))       #Profit Function V2

        

    except:
        pass
    

def make_plot(event=None):
        
    # Get these variables from outside the function, and update them.
    global gasoline_percentage_1, gasoline_percentage_2
    global lpg_percentage_1, lpg_percentage_2
    global other_percentage_1, other_percentage_2
    global max_gas, max_lpg, max_other
    global v_1, v_2, total_profit
    
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
    v_1=v_1.get()
    v_2=v_2.get()
    tp= total_profit.get()
    
    ploting_tkag.make_plot(mg,gp1,gp2,ml,lp1,lp2,mo,op1,op2,v_1,v_2,tp)
    


#==============================================================
window=Tk()

window.wm_title("Refinery Optmization")

#==============================================================Buttons

b1=Button(window,text="Calculate", width=12, command=calculate)
b1.grid(row=2,column=6)

b2=Button(window,text="Quit", width=12, command=window.destroy)
b2.grid(row=18,column=6)

b3=Button(window,text="Create Plot", width=12, command=make_plot)
b3.grid(row=4, column=6)

#===============================================================Input

l1=Label(window,text="Price Crude # 1 [$/B]")
l1.grid(row=1,column=1)

price_crude_1=DoubleVar()
e1=Entry(window,textvariable=price_crude_1)
e1.grid(row=1,column=2)

l2=Label(window,text="Phase # 1 Capacity [KBOPD]")
l2.grid(row=1,column=3)

phase_capacity_1=DoubleVar()
e2=Entry(window,textvariable=phase_capacity_1)
e2.grid(row=1,column=4)

l3=Label(window,text="Price Crude # 2 [$/B]")
l3.grid(row=2,column=1)

price_crude_2=DoubleVar()
e3=Entry(window,textvariable=price_crude_2)
e3.grid(row=2,column=2)

l4=Label(window,text="Phase # 2 Capacity [KBOPD]")
l4.grid(row=2,column=3)

phase_capacity_2=DoubleVar()
e4=Entry(window,textvariable=phase_capacity_2)
e4.grid(row=2,column=4)

l5=Label(window,text="Price Gasoline [$/B]")
l5.grid(row=3,column=1)

price_gasoline=DoubleVar()
e5=Entry(window,textvariable=price_gasoline)
e5.grid(row=3,column=2)

l6=Label(window,text="Operational Time Phase # 1 [Hrs]")
l6.grid(row=3,column=3)

operational_time_1=DoubleVar()
e6=Entry(window,textvariable=operational_time_1)
e6.grid(row=3,column=4)

l7=Label(window,text="Price LPG [$/B]")
l7.grid(row=4,column=1)

price_lpg=DoubleVar()
e7=Entry(window,textvariable=price_lpg)
e7.grid(row=4,column=2)

l8=Label(window,text="Operational Time Phase # 2 [Hrs]")
l8.grid(row=4,column=3)

operational_time_2=DoubleVar()
e8=Entry(window,textvariable=operational_time_2)
e8.grid(row=4,column=4)

l9=Label(window,text="Price Other [$/B]")
l9.grid(row=5,column=1)

price_other=DoubleVar()
e9=Entry(window,textvariable=price_other)
e9.grid(row=5,column=2)

l10=Label(window,text="Crude # 1")
l10.grid(row=7,column=2)

l11=Label(window,text="% in Decimals")
l11.grid(row=8,column=2)

l12=Label(window,text="Crude # 2")
l12.grid(row=7,column=4)

l13=Label(window,text="% in Decimals")
l13.grid(row=8,column=4)

l14=Label(window,text="ITEM")
l14.grid(row=8,column=1)

l15=Label(window,text="Gasoline")
l15.grid(row=9,column=1)

gasoline_percentage_1=DoubleVar()
e10=Entry(window,textvariable=gasoline_percentage_1)
e10.grid(row=9,column=2)

gasoline_percentage_2=DoubleVar()
e11=Entry(window,textvariable=gasoline_percentage_2)
e11.grid(row=9,column=4)

l16=Label(window,text="LPG")
l16.grid(row=10,column=1)

lpg_percentage_1=DoubleVar()
e12=Entry(window,textvariable=lpg_percentage_1)
e12.grid(row=10,column=2)

lpg_percentage_2=DoubleVar()
e13=Entry(window,textvariable=lpg_percentage_2)
e13.grid(row=10,column=4)

l17=Label(window,text="OTHER")
l17.grid(row=11,column=1)

other_percentage_1=DoubleVar()
e14=Entry(window,textvariable=other_percentage_1)
e14.grid(row=11,column=2)

other_percentage_2=DoubleVar()
e15=Entry(window,textvariable=other_percentage_2)
e15.grid(row=11,column=4)


l19=Label(window,text="Processing Cost")
l19.grid(row=12,column=1)

proccessing_cost_1=DoubleVar()
e16=Entry(window,textvariable=proccessing_cost_1)
e16.grid(row=12,column=2)

proccessing_cost_2=DoubleVar()
e17=Entry(window,textvariable=proccessing_cost_2)
e17.grid(row=12,column=4)

l20=Label(window,text="MAX KBD")
l20.grid(row=8,column=6)

max_gas=DoubleVar()
e56=Entry(window,textvariable=max_gas)
e56.grid(row=9,column=6)

max_lpg=DoubleVar()
e57=Entry(window,textvariable=max_lpg)
e57.grid(row=10,column=6)

max_other=DoubleVar()
e58=Entry(window,textvariable=max_other)
e58.grid(row=11,column=6)


l21=Label(window,text="Total")
l21.grid(row=8,column=7)

l22=Label(window,text="12 KBD")
l22.grid(row=9,column=7)

l23=Label(window,text="5 KBD")
l23.grid(row=10,column=7)

l25=Label(window,text="3 KBD")
l25.grid(row=11,column=7)


#======================================================================  Income

l34=Label(window,text="Income")
l34.grid(row=13,column=1)

l34=Label(window,text="Gasoline")
l34.grid(row=14,column=1)

l34=Label(window,text="LPG")
l34.grid(row=15,column=1)

l34=Label(window,text="Other")
l34.grid(row=16,column=1)

#====================================== Crude # 1

l60=Label(window,text="Crude # 1")
l60.grid(row=13,column=2)

income_gas_1=DoubleVar()
l35=Label(window, textvariable=income_gas_1)
l35.grid(row=14, column=2)

income_lpg_1=DoubleVar()
l36=Label(window, textvariable=income_lpg_1)
l36.grid(row=15, column=2)

income_other_1=DoubleVar()
l36=Label(window, textvariable=income_other_1)
l36.grid(row=16, column=2)
 
#=====================================Crude # 2

l60=Label(window,text="Crude # 2")
l60.grid(row=13,column=3)

income_gas_2=DoubleVar()
l37=Label(window, textvariable=income_gas_2)
l37.grid(row=14, column=3)

income_lpg_2=DoubleVar()
l38=Label(window, textvariable=income_lpg_2)
l38.grid(row=15, column=3)

income_other_2=DoubleVar()
l39=Label(window, textvariable=income_other_2)
l39.grid(row=16, column=3)

#=====================================================================   Output Volume

l26=Label(window,text="Amount Produced # A")
l26.grid(row=8,column=3)

calc_gas_1=DoubleVar()
l28=Label(window, textvariable=calc_gas_1)
l28.grid(row=9, column=3)

calc_lpg_1=DoubleVar()
l29=Label(window, textvariable=calc_lpg_1)
l29.grid(row=10, column=3)

calc_other_1=DoubleVar()
l30=Label(window, textvariable=calc_other_1)
l30.grid(row=11, column=3)

l27=Label(window,text="Amount Produced # B")
l27.grid(row=8,column=5)

calc_gas_2=DoubleVar()
l31=Label(window, textvariable=calc_gas_2)
l31.grid(row=9, column=5)

calc_lpg_2=DoubleVar()
l32=Label(window, textvariable=calc_lpg_2)
l32.grid(row=10, column=5)

calc_other_2=DoubleVar()
l33=Label(window, textvariable=calc_other_2)
l33.grid(row=11, column=5)

#================================================================ Total Income

l80=Label(window,text="Total = C # 1 + C # 2")
l80.grid(row=16,column=4)

l40=Label(window,text="Total Income")
l40.grid(row=17,column=1)

total_income_1=DoubleVar()
l41=Label(window, textvariable=total_income_1)
l41.grid(row=17, column=2)

total_income_2=DoubleVar()
l42=Label(window, textvariable=total_income_2)
l42.grid(row=17, column=3)

total_income=DoubleVar()
l43=Label(window, textvariable=total_income)
l43.grid(row=17, column=4)

l44=Label(window,text="Total Production Cost")
l44.grid(row=18,column=1)

total_production_1=DoubleVar()
l45=Label(window, textvariable=total_production_1)
l45.grid(row=18, column=2)

total_production_2=DoubleVar()
l46=Label(window, textvariable=total_production_2)
l46.grid(row=18, column=3)

total_production=DoubleVar()
l47=Label(window, textvariable=total_production)
l47.grid(row=18, column=4)

l48=Label(window,text="Total Crude Cost")
l48.grid(row=19,column=1)

crude_cost_1=DoubleVar()
l49=Label(window, textvariable=crude_cost_1)
l49.grid(row=19, column=2)

crude_cost_2=DoubleVar()
l50=Label(window, textvariable=crude_cost_2)
l50.grid(row=19, column=3)

total_crude_cost=DoubleVar()
l51=Label(window, textvariable=total_crude_cost)
l51.grid(row=19, column=4)

l52=Label(window,text="Profit")
l52.grid(row=20,column=1)

profit_1=DoubleVar()
l53=Label(window, textvariable=profit_1)
l53.grid(row=20, column=2)

profit_2=DoubleVar()
l54=Label(window, textvariable=profit_2)
l54.grid(row=20, column=3)

total_profit=DoubleVar()
l55=Label(window, textvariable=total_profit)
l55.grid(row=20, column=4)


#================================================= Profit Function

#For Volume 1

l100=Label(window,text="Profit Function")
l100.grid(row=16,column=5)

l101=Label(window,text="V1")
l101.grid(row=17,column=5)

v_1=DoubleVar()
l102=Label(window, textvariable=v_1)
l102.grid(row=18, column=5)


#For Volume 2

l103=Label(window,text="V2")
l103.grid(row=19,column=5)

v_2=DoubleVar()
l104=Label(window, textvariable=v_2)
l104.grid(row=20, column=5)


window.mainloop()
