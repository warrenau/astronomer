# data processing classes and functions

import numpy as np
import matplotlib.pyplot as plt

# define class
class Data(object):
    """Data over time for one or more positions.

    Attributes
    ----------
    t : time in units of [s]
    d : data
    p : the name of the locations
    """ 
    def __init__(self, time, data, positions):
        """Initializes the density data with supplied values for time, density data, and location names."""
        self.t = time
        self.d = data
        self.p = positions


# take data from csv file and convert into Data class to be used by other functions
def csv_to_data(filename, positions):
    """ Takes data from csv and converts to Data class.
    Parameters
    ----------
    filename : string
        name of file to be read in.
    positions : string
        names of positions or locations for data, like a header.

    Returns
    -------
    data : Data
        Formatted data from csv file.

    """
    data_read = np.genfromtxt(filename, delimiter=',')
    time = data_read[1:,0]
    data_in = data_read[1:,1:]

    data = Data(time, data_in, positions)
    return data


# plot data from Data class
def plot_density(data, filename):
    """ Plots density from data in Data class format into png, svg, and pdf formats.
    Parameters
    ----------
    filename : string
        name of file to be saved to
    """
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['mathtext.fontset'] = 'dejavuserif'
    plt.figure(facecolor='w', edgecolor='k', dpi=300)
    for k in range(len(data.p)):
        plt.plot(data.t, data.d[:,k], label=data.p[k])
    plt.xlabel(r'Time ($s$)')
    plt.ylabel(r'Density ($kg/m^3$)')
    plt.figlegend(loc='lower right', bbox_to_anchor=(0.95,0.15))
    plt.grid(b=True, which='major', axis='both')
    plt.tight_layout()
    plt.savefig(filename+'_plot.png',transparent=True)
    plt.savefig(filename+'_plot.svg',transparent=True)
    plt.savefig(filename+'_plot.pdf',transparent=True)

def plot_pressure(data, filename):
    """ Plots pressure from data in Data class format into png, svg, and pdf formats.
    Parameters
    ----------
    filename : string
        name of file to be saved to
    """
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['mathtext.fontset'] = 'dejavuserif'
    plt.figure(facecolor='w', edgecolor='k', dpi=300)
    for k in range(len(data.p)):
        plt.plot(data.t, data.d[:,k], label=data.p[k])
    plt.xlabel(r'Time ($s$)')
    plt.ylabel(r'Pressure ($Pa$)')
    plt.figlegend(loc='lower right', bbox_to_anchor=(0.95,0.15))
    plt.grid(b=True, which='major', axis='both')
    plt.tight_layout()
    plt.savefig(filename+'_plot.png',transparent=True)
    plt.savefig(filename+'_plot.svg',transparent=True)
    plt.savefig(filename+'_plot.pdf',transparent=True)


def plot_temperature(data, filename):
    """ Plots temperature from data in Data class format into png, svg, and pdf formats.
    Parameters
    ----------
    filename : string
        name of file to be saved to
    """
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['mathtext.fontset'] = 'dejavuserif'
    plt.figure(facecolor='w', edgecolor='k', dpi=300)
    for k in range(len(data.p)):
        plt.plot(data.t, data.d[:,k], label=data.p[k])
    plt.xlabel(r'Time ($s$)')
    plt.ylabel(r'Temperature ($K$)')
    plt.figlegend(loc='upper left', bbox_to_anchor=(0.2,0.8))
    plt.grid(b=True, which='major', axis='both')
    plt.tight_layout()
    plt.savefig(filename+'_plot.png',transparent=True)
    plt.savefig(filename+'_plot.svg',transparent=True)
    plt.savefig(filename+'_plot.pdf',transparent=True)

# function to convert units to atom/b-cm for MCNP
def density_to_atomdensity(data_in):
    """ Converts density in kg/m^3 to atom/barn-cm for helium-3.
    Parameters
    ----------
    data_in : Data
        Density over time in kg/m^3 in Data class format.

    Returns
    -------
    data_out : Data
        Density over time in atom/b-cm in Data class format.
    """
    data_out = Data(data_in.t, data_in.d, data_in.p)
    data_out.d = data_in.d * 1000 * 6.022e23 * 1e-6 * 1e-24 / 3.016029
    return data_out



# function to get time step data for MCNP input
def get_time_step_data(data_in, time_step):
    """ Sparses data file for time steps specified by user.

    Parameters
    ----------
    data_in : Data
        Data to be condensed into time steps
    time_step : float
        Time steps requested.

    Returns
    -------
    data_out : Data
        Data in specified time steps.
    """
    data_out = Data(np.zeros((len(time_step)+2)), np.zeros((len(time_step)+2, len(data_in.p))), data_in.p)

    data_out.t[0] = data_in.t[0]
    data_out.t[-1] = data_in.t[-1]

    data_out.d[0] = data_in.d[0]
    data_out.d[-1] = data_in.d[-1]

    data_index = 0
    time = 0
    for k in range(len(time_step)):
        
        while time < time_step[k] and data_index < len(data_in.t):
            time = data_in.t[data_index]
            data_index += 1
        
        data_out.t[k+1] = time
        data_out.d[k+1] = data_in.d[data_index-1]

    return data_out



# write Data class data to file
def writeData(data, filename):
    """ Writes Data class data to csv file.
    """
    data_out = np.zeros((len(data.t),len(data.d[0,:])+1))
    data_out[:,0] = data.t
    data_out[:,1:] = data.d
    with open(filename, 'w') as f:
        f.write('Time,'+','.join(data.p)+'\n' )
        np.savetxt(f, data_out, delimiter=',', newline='\n')
