#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Daisy World
# =============================================================================

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import sys
if sys.version[:1] == '3':
    raw_input = input
    
    
#%%

## set parameters for daisies
#opt_temp = float(raw_input("what variable do you want to use for optimal growing temperature? to use default enter 0 (default = 22.5)?: "))
#
#if opt_temp == 0:
#    opt_temp = 22.5
#
#growth_rate_temp = float (raw_input("what growing rate parameter as function of temp do you want? to use default enter 0 (default = 0.003265)?: "))
#
#if growth_rate_temp == 0:
#    growth_rate_temp = 0.003265

#%%
# =============================================================================
# Initialize model and set parameters
# =============================================================================
growth_rate_temp = 0.003265
# initializing start values of daisies
BD_area = 0.01
WD_area = 0.01
# set global constants
solar_constant = 1000
barren_albedo = 0.5
Stefan_Boltzmann = 5.67e-08
# set daisy parameters 
hor_ins = 20
deathrate = 0.2 # <-- this is correct
dt = 1.



#now that we have our variables we start a loop that will find an equilibrium for every given value of Luminisity (L)
#the values of L we will use range from 0.5 to 1.7 with intervals of 0.01:

# =============================================================================
# Loop over all luminosities
# =============================================================================
def daisy_world(luminosity_range, WD_area, BD_area, opt_temp_W, opt_temp_B, WD_albedo, BD_albedo):
    # intitalizing lists to store intermediate/output
    eq_temperature = []
    eq_area_WD = []
    eq_area_BD = []
    temp_log_no_daisy = []
    for L in luminosity_range:
    #    # initializing start values of daisies
    #    BD_area = 0.01
    #    WD_area = 0.01
        
        Convergence = False
        n = 0
        while Convergence == False:
            n += 1
            # =====================================================================
            # Solve equations for single L
            # =====================================================================
            
            # 1 find planetary albedo
            DW_fertile_land = 1-(WD_area + BD_area)
            DW_albedo = (barren_albedo * DW_fertile_land) + (WD_albedo * WD_area) + (BD_albedo * BD_area)
            
            # 2 find planetary temperature
            DW_temperature = ((solar_constant * L * (1-DW_albedo)) / (Stefan_Boltzmann))**0.25
            
            # 3 find local temperature of daisies
            # converted to C since the equationg only works with celsius:
            WD_localtemp = (hor_ins*(DW_albedo-WD_albedo) + (DW_temperature)) 
            BD_localtemp = (hor_ins*(DW_albedo-BD_albedo) + (DW_temperature)) 
            
            # 4 find birthrate for daisy
            #prevent negative birthrate with standard python function max(a,b) 
            dWD_birth = max(0,1-growth_rate_temp*(opt_temp_W - WD_localtemp)**2) * dt
            dBD_birth = max(0,1-growth_rate_temp*(opt_temp_B - BD_localtemp)**2) * dt
            
            # 5 calulate change in daisy areas due to birth and death
            dWD_area = WD_area * (DW_fertile_land * dWD_birth - deathrate)
            dBD_area = BD_area * (DW_fertile_land * dBD_birth - deathrate)
            
            # 6 update area's
            #using forward Euler method to approximate differential equation for incease in area over time:
            WD_area += dWD_area * dt
            BD_area += dBD_area * dt
            # ensure that daisys area is >= 0.01, since too lower values will mean
            # no seeds are available on the planet for growing 
            WD_area = max(0.01, WD_area)
            BD_area = max(0.01, BD_area)
            
            # 7 calculate new albedo
            DW_fertile_land = 1-(WD_area + BD_area)
            DW_albedo = (barren_albedo * DW_fertile_land) + (WD_albedo * WD_area) + (BD_albedo * BD_area)
            
            # 8 calulate new temperature 
            DW_temp_next = ((solar_constant * L * (1-DW_albedo)) / (Stefan_Boltzmann))**0.25
    
            # 9 check for convergence of Daisy World temperature 
            Convergence = abs(DW_temperature - DW_temp_next)<1E-6
            
            # 10 temperature without daisies
            no_daisy_temp = ((solar_constant * L * (1-0.5)) / (Stefan_Boltzmann))**0.25
            
            if n > 2000:
                Convergence = True
                print('reached max convergence iterations')
            
    #        if Convergence == True:
    #            print('number of steps before congvergence')
    #            print(n)
    #    
        # =============================================================================
        # save the equilibrium variables for each L
        # =============================================================================
        eq_temperature.append(DW_temp_next)
        eq_area_WD.append(WD_area)
        eq_area_BD.append(BD_area)
        temp_log_no_daisy.append(no_daisy_temp)
    return eq_temperature, eq_area_WD, eq_area_BD, temp_log_no_daisy
    




WD_albedo = 0.8
BD_albedo = 0.25
opt_temp_W = 22.5
opt_temp_W += 273.15
opt_temp_B = 10.5
opt_temp_B += 273.15


luminosity_range = np.arange(0.2, 1.8, 0.002)
luminosity_range = luminosity_range[::-1]

eq_temperature, eq_area_WD, eq_area_BD, temp_log_no_daisy = daisy_world(
        luminosity_range, WD_area, BD_area, opt_temp_W, opt_temp_B, WD_albedo, BD_albedo)
                                                                
# =============================================================================
# two example plots of the output using the matplotlib python library:    
# ============================================================================
plt.figure()
plt.plot(luminosity_range, eq_temperature, label='Temperature with daisies')
plt.plot(luminosity_range, temp_log_no_daisy, label='Temperature no daisies')
plt.xlabel('Luminosity')
plt.ylabel('Temperature (K)')
plt.title("Equilibrium temperature (K) for given L")
plt.legend()
plt.show()

plt.figure()
plt.plot(luminosity_range, eq_area_WD, label='white daisies')
plt.plot(luminosity_range, eq_area_BD, label='black daisies')
plt.xlabel('Luminosity')
plt.ylabel('Fraction of coverage')
plt.title("Equilibrium coverage of the daisies for given L")
plt.legend()
plt.show()



#%%



