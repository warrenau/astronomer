# this is the main script for astronomer
# here you will call other scripts and functions to process the data you want
# this script can be modified directly (or, when I get it working, use an input file)

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from density import *


# read in data
filepath = 'astronomer/Data/'
filename = 'BOT2HENRIDensity'
f = filepath+filename+'.csv'

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005])


##########
# this part of the script will determine what other scripts need to be called
# this will depend on what outputs you are trying to process
##########



##########
# this part of the script will run the other scripts needed to process the data
# this includes scripts for plotting, storing data, and even generating reports
##########


#
density_data = plot_data(filename, positions)

atomdensity_data = density_to_atomdensity(density_data)

density_data_step = get_time_step_data(atomdensity_data, time_step)

writeDensity(density_data_step, filepath+filename+'_step.csv')

