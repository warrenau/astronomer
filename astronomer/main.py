# this is the main script for astronomer
# here you will call other scripts and functions to process the data you want
# this script can be modified directly (or, when I get it working, use an input file)

import numpy as np
import matplotlib.pyplot as plt
import density as dens


# inputs
filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_HeatGen_TS_density'
f = filepath+filename+'.csv'

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])



# functions
density_data = dens.data_to_density(f,positions)
dens.plot_data(density_data, filename)
atomdensity_data = dens.density_to_atomdensity(density_data)
atomdensity_data_step = dens.get_time_step_data(atomdensity_data, time_step)
dens.writeDensity(atomdensity_data_step, filepath+filename+'_step.csv')
