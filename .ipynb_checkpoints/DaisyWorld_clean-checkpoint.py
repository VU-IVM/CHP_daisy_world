#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Daisy World
# =============================================================================

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import sys

# =============================================================================
# Initialize model and set parameters
# =============================================================================

# set daisy parameters 
growth_rate_temp = 0.003265
hor_ins = 20 
deathrate = 0.2 
WD_albedo = 0.75 # White Daisies albedo
BD_albedo = 0.25 # Black Daisies albedo
opt_temp_W = 22.5 # optimal temperature for White daisies
opt_temp_W += 273.15 # Convert to Kelvin
opt_temp_B = 10.5 # optimal temperature for Black daisies
opt_temp_B += 273.15 # Convert to Kelvin
growth_rate_temp = 0.003265

# initializing start values of daisies
BD_area = 0.01
WD_area = 0.01

# intitalizing lists to store intermediate/output
eq_temperature = []
eq_area_WD = []
eq_area_BD = []
temp_log_no_daisy = []

# set global constants
solar_constant = 1000
barren_albedo = 0.5
dt = 1.
# create a sequence of numbers (i.e. an array) using the numpy python library
luminosity_range = np.arange(0.5, 1.7, 0.002)
#luminosity_range = luminosity_range[::-1] <-- to reverse the array, needed for next practicum
Stefan_Boltzmann = 5.67e-08







#now that we have our variables we start a loop that will find an equilibrium for every given value of Luminisity (L)
#the values of L we will use range from 0.5 to 1.7 with intervals of 0.002:

# =============================================================================
# Loop over all luminosities
# =============================================================================

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
        DW_fertile_land = 
        DW_albedo = 
        
        # 2 find planetary temperature
        DW_temperature = 
        
        # 3 find local temperature of daisies
        WD_localtemp = 
        BD_localtemp = 
        
        # 4 find birthrate for daisy
        #prevent negative birthrate with standard python function max(a,b) 
        dWD_birth = 
        dBD_birth = 
        
        # 5 calulate change in daisy areas due to birth and death
        dWD_area = 
        dBD_area = 
        
        # 6 update area's
        #using forward Euler method to approximate differential equation for incease in area over time:
        WD_area += (WD_area * (DW_fertile_land * dWD_birth - deathrate)) 
        BD_area += (BD_area * (DW_fertile_land * dBD_birth - deathrate)) 
        # ensure that daisys area is >= 0.01 with max(a,b) function, since too lower values 
        # will mean no seeds are available on the planet for growing 
        WD_area = 
        BD_area = 
        
        # 7 calculate new albedo
        DW_fertile_land = 
        DW_albedo = 
        
        # 8 calulate new temperature 
        DW_temp_next = 

        # 9 check for convergence of Daisy World temperature 
        Convergence = abs(DW_temperature - DW_temp_next)<1E-6
        
        # 10 temperature without daisies
        no_daisy_temp = ((solar_constant * L * (1-0.5)) / (Stefan_Boltzmann))**0.25
 
#        if Convergence == True:
#            print(n) # to print number of steps before convergence')
    
    # =============================================================================
    # save the equilibrium variables for each L into list generated at the beginning
    # =============================================================================
    eq_temperature.append(DW_temp_next)
    eq_area_WD.append(WD_area)
    eq_area_BD.append(BD_area)
    temp_log_no_daisy.append(no_daisy_temp)


# =============================================================================
# two example plots of the output using the matplotlib python library:    
# =============================================================================
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




