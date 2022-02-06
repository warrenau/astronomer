# this is a script/function to process the density data
# will need inputs of file paths to use -- this should be based on constelation

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# define class
class Density(object):
    """Data over time for one or more positions.

    Attributes
    ----------
    t : time in units of [s]
    d : density in units of [kg/m^3]
    p : the name of the locations
    """ # I want a way of including the header / position information, but Im not sure how rn

    def __init__(self, time, data, positions):
        """Initializes the density data with supplied values for time, density data, and location names."""
        self.t = time
        self.d = data
        self.p = positions

# dont use line probe data -- use the monitor csv files that have data for each position


# read in data
filepath = 'astronomer/Data/'
filename = 'BOT2HENRIDensity'
f = filepath+filename+'.csv'

data_read = np.genfromtxt(f, delimiter=',')
# need to define class or something to handle data
time = data_read[1:,0]
data_in = data_read[1:,1:]
positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

data = Density(time, data_in, positions)

# plot the data
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.figure(facecolor='w', edgecolor='k', dpi=200)
for k in range(len(data.p)):
    plt.plot(data.t, data.d[:,k], label=data.p[k])
plt.xlabel('Time (s)')
plt.ylabel('Density (kg/m^3)')
plt.figlegend(loc='upper left', bbox_to_anchor=(0.2,0.8))
plt.grid(b=True, which='major', axis='both')
plt.savefig(filepath+filename+'_plot.png',transparent=True)
plt.savefig(filepath+filename+'_plot.svg',transparent=True)

# function to convert units to atom/b-cm for MCNP


# store the data as hdf5?