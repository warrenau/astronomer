# astronomer

Processes data from CONSTELATION coupled model. CONSTELATION couples the CFD code, STAR-CCM+, and the reactor physics code, Serpent 2. So far, only CFD output processing has been implemented.

## Usage

To use the package, clone the repository to your local machine and add the data files to */astronomer/Data/*. The data files are expected to be in the format of a header over each column, a time column on the left, then data columns. This is consistent with exporting a tabulated plot in STAR-CCM+. Modify the *main.py* file to include the correct inputs for your data file(s) and the desired functions.

### Inputs

The input options are: `filepath`, `filename`, `positions`, and `time_step`.

`filepath`: the path to the data files.
```
filepath = 'astronomer/Data/'
```

`filename`: name of file to be read in.
```
filename = 'HENRI_250psi_HeatGen_TS_density'
```

`positions`: header for data (positions on experiment). This should be the same length as the data columns.
```
positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')
```

`time_step`: requsted time steps for atom density output. This will need to be changed for each data file. The first time step must be greater than the first data entry in the file and the last time step must be smaller than the last data entry in the file. The requested time steps can otherwise be any value in between. The function will find the nearest data value to the request time step, so the input does not need to be exact.
```
time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])
```

### Classes

There is currently only one class defined in this package. The `Density` class holds the time, data, and positions header for a given set of density data and makes them easily accesible. The functions used in the package use this class.
```
data = Density(time, data_in, positions)
```
The first argument is the time array, called by `data.t`; the second is the density values array, called by `data.d`; and the third is the positons tuple, called by `data.p`.

### Functions

There are five (5) functions defined in *density.py*. Each utilizes the inputs above and the `Density` class.

`data_to_density`: takes data from csv file and stores it as a `Density` class object. The first argument is the filepath for the data file. The second argument is the positions header tuple.
```
density_data = dens.data_to_density(f,positions)
```

`plot_data`: plots the data stored in the given `Density` class object. The first argument is the `Density` class object of interest. The second argument is the filename to be used as a base for the plot filename. The default value is the `filename` input.
```
dens.plot_data(density_data, filename)
```

`density_to_atomdensity`: converts the input data from density in kilogram per cubic meter to atom density in atoms per barn-centimeter. The input is a `Density` class object. The output is also a `Density` class object.
```
atomdensity_data = dens.density_to_atomdensity(density_data)
```

`get_time_step_data`: retrieves data at specified time values. The first argument is the `Density` class object that the user desires specific time steps from. The second argument is array of specified time values input by the user. The function simply retrieves the time value and data values closest to the requested time without exceeding it. For the data this package was designed for, this is not an issue because the time steps are very small.
```
atomdensity_data_step = dens.get_time_step_data(atomdensity_data, time_step)
```

`writeDensity`: writes a `Density` class object out to a *.csv* file. The first argument is the `Density` class object to be written. The second argument is the path of the file to write to. By default, this is made by combining the input `filepath` and `filename`, then adding '*_step.csv*', as seen below.
```
dens.writeDensity(atomdensity_data_step, filepath+filename+'_step.csv')
```