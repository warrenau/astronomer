# this is a script/function to process the density data
# will need inputs of file paths to use -- this should be based on constelation

import numpy as np
import matplotlib.pyplot as plt

# need to read in data from csv files located in \LineProbe; \LineProbeBot; and \LineProbeTop
# axial data is denoted as: Line_Probe_Density_Line_Dens_00100.csv
# radial data is denoted as: Radial_Line_Density_RadialDens_00100.csv
# where _00100 at end of file name is time step, increments by 100 in folders
# plot density vs time with a line for each data position on the physical experiment (I will have to find the correct positions)
# plotting all of the time steps might not be reasonable if there are a lot -- this script or the main program should be somewhat adaptive to make good looking plots

# read in data one file at a time -- how?
# some sort of for loop? for file in folder?
# set upper time step limit manually? -- can this be done automatically
min_step = 100
max_step = 10300

for f in range(max_step/min_step):
    filename = "Line_Probe_Density_Line_Dens_"+str('%05.0f' %(100*(f+1)))+".csv"
    