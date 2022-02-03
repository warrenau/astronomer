# this is a script/function to process the density data
# will need inputs of file paths to use -- this should be based on constelation

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# need to read in data from csv files located in \LineProbe; \LineProbeBot; and \LineProbeTop
# axial data is denoted as: Line_Probe_Density_Line_Dens_00100.csv
# radial data is denoted as: Radial_Line_Density_RadialDens_00100.csv
# where _00100 at end of file name is time step, increments by 100 in folders
# plot density vs time with a line for each data position on the physical experiment (I will have to find the correct positions)
# plotting all of the time steps might not be reasonable if there are a lot -- this script or the main program should be somewhat adaptive to make good looking plots
#folder = Path("astronomer/LineProbe/")


# read in data one file at a time -- how?
# some sort of for loop? for file in folder?
# set upper time step limit manually? -- can this be done automatically
min_step = 100
max_step = 10300
num_steps = int(max_step/min_step)


for j in range(num_steps):
    # generate file name
    filename = "astronomer/LineProbe/Line_Probe_Density_LineDens_"+str('%05.0f' %(100*(j+1)))+".csv"
    #f = folder / filename
    # read in file
    dens_step = np.genfromtxt(filename, delimiter=',',skip_header=1)

    # set up array of zeros based on size of read in files
    if j == 0:
        x_num = len(dens_step[:,0]) # find length of x values
        dens = np.zeros((x_num+1, num_steps + 1)) # set array of zeros
        dens[:,0] = dens_step[:,0] # fill in x values
        dens[0,1:] = np.linspace(min_step, max_step, num_steps)

    # fill in with values from file read in this loop
    dens[1:,j+1] = dens_step[:,1]
    print(dens)
