# astronomer

***astronomer*** processes data from CONSTELATION coupled model. CONSTELATION couples the CFD code, STAR-CCM+, and the reactor physics code, Serpent 2. So far, only CFD output processing has been implemented. Processing functions for Serpent 2 results can be found in the `serpentTools` package (https://serpent-tools.readthedocs.io/en/master/).

## Usage

Install the package from PyPI using `pip` and import into your processing script.

```
pip install constelation_astronomer
```

```python
import constelation_astronomer.astronomer as astro
```

### Classes

There is one class defined in this package. The `Data` class holds the time, data, and positions header for a given set of data and makes them easily accesible. The functions used in the package use this class.
```python
data = Data(time, data_in, positions)
```
The first argument is the time array, called by `data.t`; the second is the data values array, called by `data.d`; and the third is the positons tuple, called by `data.p`.

### Functions

There are seven (7) functions defined in the package, three of the functions are plotting functions that have different labels for the different measured parameters.

---

`csv_to_data`: takes data from csv file and stores it as a `Data` class object. The first argument is the data file, expressed as a path from where the code is running. The second argument is the positions header tuple.
```python
density_data = astro.csv_to_data(filename,positions)
```

---
`plot_density`, `plot_pressure`, and `plot_temperature`: plots the data stored in the given `Data` class object. The first argument is the `Data` class object of interest. The second argument is the filename to be used as a base for the plots. The function will append *`_plot`* to the input filename before saving.
```python
astro.plot_density(density_data, filename)
```

---
`density_to_atomdensity`: converts the input data from density in kilogram per cubic meter to atom density in atoms per barn-centimeter, specifically for helium-3. The input is a `Data` class object. The output is also a `Data` class object.
```python
atomdensity_data = astro.density_to_atomdensity(density_data)
```

---
`get_time_step_data`: retrieves data at specified time values. The first argument is the `Data` class object that the user desires specific time steps from. The second argument is an array of specified time values input by the user. The function simply retrieves the time value and data values closest to the requested time without exceeding it. For the data this package was designed for, this is not an issue because the time steps are very small.
```python
atomdensity_data_step = astro.get_time_step_data(atomdensity_data, time_step)
```

---
`writeData`: writes a `Data` class object out to a *.csv* file. The first argument is the `Data` class object to be written. The second argument is the path of the output file. A suggested naming scheme is made by appending '*_step.csv*' to the file that was read in originally, as seen below.
```python
astro.writeData(atomdensity_data_step, filename+'_step.csv')
```


## Examples

The functions described above can be used in any combination the user wishes, as long as the data is stored in a `Data` object. These functions can also be used for multiple data files. Below are some examples.


This first example will read in data from *astronomer/Data/HENRI_250psi_TS_density.csv*, plot the data over time, convert the density data into atom density, find the atom density data at requested time values, then write the requested values to a *.csv* file.
```python
import constelation_astronomer.astronomer as astro

filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_HeatGen_TS_density'
f = filepath+filename+'.csv'

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])

density_data = astro.data_to_density(f,positions)
astro.plot_data(density_data, filename)
atomdensity_data = astro.density_to_atomdensity(density_data)
atomdensity_data_step = astro.get_time_step_data(atomdensity_data, time_step)
astro.writeData(atomdensity_data_step, filepath+filename+'_step.csv')
```

---
This next example shows what it looks like to process multiple files that are using the same headers and requested time steps.
```python
import constelation_astronomer.astronomer as astro

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])

# 250 psi Heat Gen
filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_HeatGen_Dens_TS'
f = filepath+filename+'.csv'

density_data = astro.data_to_density(f,positions)
astro.plot_data(density_data, filename)

atomdensity_data = astro.density_to_atomdensity(density_data)
atomdensity_data_step = astro.get_time_step_data(atomdensity_data, time_step)
astro.writeData(atomdensity_data_step, filepath+filename+'_step.csv')


# 250 psi no Heat Gen
filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_noHeatGen_Dens_TS'
f = filepath+filename+'.csv'

density_data = astro.data_to_density(f,positions)
astro.plot_data(density_data, filename)

atomdensity_data = astro.density_to_atomdensity(density_data)
atomdensity_data_step = astro.get_time_step_data(atomdensity_data, time_step)
astro.writeData(atomdensity_data_step, filepath+filename+'_step.csv')
```

---
Finally, this third example shows using the `get_time_step_data` and `writeData` functions for more than one `Data` object.
```python
import constelation_astronomer.astronomer as astro

filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_HeatGen_TS_density'
f = filepath+filename+'.csv'

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')

time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])

density_data = astro.data_to_density(f,positions)
astro.plot_data(density_data, filename)
density_data_step = astro.get_time_step_data(density_data, time_step)
astro.writeData(density_data_step, filepath+filename+'_step.csv')

atomdensity_data = astro.density_to_atomdensity(density_data)
atomdensity_data_step = astro.get_time_step_data(atomdensity_data, time_step)
astro.writeData(atomdensity_data_step, filepath+filename+'_atomdensity_step.csv')
```
