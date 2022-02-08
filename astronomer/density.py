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

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

def plot_data(filename, positions):
    """ Plots data from csv file into png and svg formats.
    Parameters
    ----------
    filename : string
        name of file to be plotted
    positions : string
        names of positions or locations for data, like a header.

    Returns
    -------
    data : Density
        Formatted data from csv file. # maybe this should be a separate function.
    """

    filepath = 'astronomer/Data/'
    f = filepath+filename+'.csv'

    data_read = np.genfromtxt(f, delimiter=',')
    # need to define class or something to handle data
    time = data_read[1:,0]
    data_in = data_read[1:,1:]


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

    return data

# function to convert units to atom/b-cm for MCNP
def density_to_atomdensity(data_in):
    """ Converts density in kg/m^3 to atom/barn-cm for helium-3.
    Parameters
    ----------
    data_in : Density
        Density over time in kg/m^3 in Density class format.

    Returns
    -------
    data_out : Density
        Density over time in atom/b-cm in Density class format.
    """
    data_out = Density(data_in.t, data_in.d, data_in.p)
    data_out.d = data_out * 1000 * 6.022e23 * 1e-6 * 1e-24 / 3.016029
    return data_out



# function to get time step data for MCNP input
def get_time_step_data(data_in):
    """ Sparses data file for time steps approx every 1 millisecond.

    Parameters
    ----------
    data_in : Density
        Data to be condensed into 1 ms time steps

    Returns
    -------
    data_out : Density
        Data in 1 ms time steps.
    """
    # look up old scripts for this. should be pretty similar. maybe try to add dynamic adjustments, but not sure how.


# store the data as hdf5?