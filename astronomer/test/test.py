# test functions

# import packages
import numpy as np
from density import *


# go from density to atom density
def test_atomdensity():
    t = np.array([0, 0.001, 0.002, 0.003, 0.004, 0.005])
    d = np.array([0, 1, 1.5, 3, 10, 1e3, -2])
    p = ('test')
    data = Density(t,d,p)

    atom_data = density_to_atomdensity(data)

    test_data = d  * 1000 * 6.022e23 * 1e-6 * 1e-24 / 3.016029

    assert atom_data.d == test_data


# test time step sparsing function
def test_step_data():
    t = np.array([0, 0.0003, 0.0012, 0.0017, 0.0021, 0.0028, 0.0032, 0.0036, 0.004, 0.0043])
    d = np.array([1e0, 3e0, 1e1, 7e1, 1e2, 2e2, 1e3, 4e3, 1e4, 4e4])
    p = ('test')
    data = Density(t,d,p)
    time_step = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008])

    step_data = get_time_step_data(data, time_step)

    test_d = np.array([1e0,1e1,1e2,1e3,1e4,4e4])
    test_t = np.array([0, 0.0012, 0.0021, 0.0032, 0.004, 0.0043])
    test_data = Density(test_t, test_d, p)


    assert step_data == test_data
