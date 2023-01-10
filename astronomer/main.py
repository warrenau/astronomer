# this is the main script for astronomer
# here you will call other scripts and functions to process the data you want
# this script can be modified directly

# packages
import numpy as np
import matplotlib.pyplot as plt
import astronomer.astronomer as astro


# inputs
filepath = 'astronomer/Data/'
filename = 'HENRI_250psi_noHeatGen_Press_TS'
ostr_filename = '1e-2cm_Pressure_35000000'
f = filepath+filename+'.csv'
ostr_f = filepath+ostr_filename+'.csv'

positions = ('TS00', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05')
henri_coordinates = np.array([1.663065, 1.967865, 2.107565, 2.272665, 2.577465, 3.225165]) - 1.45

ostr_positions = ('DV01', 'DV02', 'TS01', 'TS02', 'TS03', 'TS04')
ostr_coordinates = np.array([0.35, 0.56, 0.77, 0.98]) - 0.346436


# functions
# pressure_data_henri = astro.csv_to_data(f,positions)
# astro.plot_pressure(pressure_data_henri, filename)

pressure_data_ostr = astro.csv_to_data(ostr_f,ostr_positions)
astro.plot_pressure(pressure_data_ostr, ostr_filename)



ostr_filename = '1e-2cm_Density_35000000'
ostr_f = filepath+ostr_filename+'.csv'

density_data_ostr = astro.csv_to_data(ostr_f,ostr_positions)
astro.plot_density(density_data_ostr, ostr_filename)
# # non dim stuff
# gamma = 1.667
# M = 3.016029
# T = 300
# R = 8.3144598
# speed_of_sound = np.sqrt(gamma*R*T/M)
# henri_length = 1.8288 # length of henri test section and reflector in m
# henri_totlength = 3.325165  # length of henri at TS05
# henri_tau = henri_totlength / speed_of_sound
# #henri_tau = 0.008
# ostr_length = 0.638   # length of ostr henri test section in m
# ostr_totlength = 0.984 # length of ostr henri at TS04
# ostr_tau = ostr_totlength / speed_of_sound
# #ostr_tau = 0.001

# pressure_data_henri.t = pressure_data_henri.t / henri_tau
# pressure_data_ostr.t = pressure_data_ostr.t / ostr_tau

# pressure_data_henri.d = pressure_data_henri.d * 6894.76 / 1.724e6 # convert from psia to Pa
# pressure_data_ostr.d = pressure_data_ostr.d / 1.724e6

# print(1.127465/henri_length)
# print(0.423564/ostr_length)

# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['mathtext.fontset'] = 'dejavuserif'
# plt.figure(facecolor='w', edgecolor='k', dpi=300)
# plt.plot(pressure_data_henri.t, pressure_data_henri.d[:,4],'-k', label='HENRI-'+pressure_data_henri.p[4])
# plt.plot(pressure_data_ostr.t, pressure_data_ostr.d[:,4],'-b', label='OSTR-'+pressure_data_ostr.p[4])
# plt.xlabel(r'Time ($t/\tau$)')
# plt.ylabel(r'Pressure ($P/P_0$)')
# plt.figlegend(loc='upper left', bbox_to_anchor=(0.6,0.25))
# plt.grid(b=True, which='major', axis='both')
# plt.savefig('astronomer/plots/'+'NonDim_totlength_comp'+'_plot.pdf',transparent=True)