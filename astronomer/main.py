# this is the main script for astronomer
# here you will call other scripts and functions to process the data you want
# this script can be modified directly (or, when I get it working, use an input file)

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import density as dens


# read in data
filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_HeatGen_TS_density'
f = filepath+filename+'.csv'

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])


##########
# this part of the script will determine what other scripts need to be called
# this will depend on what outputs you are trying to process
##########



##########
# this part of the script will run the other scripts needed to process the data
# this includes scripts for plotting, storing data, and even generating reports
##########


#
density_data = dens.data_to_density(f,positions)

dens.plot_data(density_data, filename)

atomdensity_data = dens.density_to_atomdensity(density_data)

density_data_step = dens.get_time_step_data(atomdensity_data, time_step)

dens.writeDensity(density_data_step, filepath+filename+'_step.csv')



t = np.array([0, 0.0003, 0.0012, 0.0017, 0.0021, 0.0028, 0.0032, 0.0036, 0.004, 0.0043])
d = np.array([1e0, 3e0, 1e1, 7e1, 1e2, 2e2, 1e3, 4e3, 1e4, 4e4])
p = ('test',)
data = dens.Density(t,d,p)
time_step = np.array([0.001, 0.002, 0.003, 0.004])

step_data = dens.get_time_step_data(data, time_step)

test_d = np.array([1e0,1e1,1e2,1e3,1e4,4e4])
test_t = np.array([0, 0.0012, 0.0021, 0.0032, 0.004, 0.0043])
test_data = dens.Density(test_t, test_d, p)
print(step_data.t)
print(test_data.t)
print(step_data.d)
print(test_data.d)