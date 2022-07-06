import numpy
import matplotlib
import matplotlib as plt
D_air = [0.23, 0.31, 0.44, 0.51, 0.62, 0.77, 0.80]
D_naplus = [0.01, 0.02, 0.05, 0.07, 0.08, 0.13, 0.14]
T = [300,310,320,330,340,350,360]
font = {'family' : 'normal',
'weight' : 'bold',
'size' : 22}
plt.plot(T,D_air,color="forestgreen",label="Air")
plt.plot(T,D_naplus,color="blue",label="Ion natrium")
plt.xlabel("$T$ [K]")
plt.ylabel("$D$ [Angstrom$^2$/ps]")
plt.show()