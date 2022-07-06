import numpy as np
x = np.arange(0,100,0.001)
y = np.sin(x)
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()
plt.xlabel("x")
plt.ylabel("y")  
plt.show()
plt.scatter(x,y)
plt.xlabel(x)
plt.ylabel(y)
plt.xlim(0,10)
plt.show()
import matplotlib
font = {'family' : 'normal',
'weight' : 'bold',
'size' : 22}
matplotlib.rc('font', **font)
plt.scatter(x,y,color="red")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0,10)
plt.plot(x,y, 's-*')
plt.show()
import matplotlib.pyplot as plt
font = {'family' : 'normal',
'weight' : 'bold',
'size' : 22}
matplotlib.rc('font', **font)
D_air = [0.23, 0.31, 0.44, 0.51, 0.62, 0.77, 0.80]
D_naplus = [0.01, 0.02, 0.05, 0.07, 0.08, 0.13, 0.14]
T = [300,310,320,330,340,350,360]
plt.plot(T,D_air,color="forestgreen",label="Air")
plt.plot(T,D_naplus,color="blue",label="Ion natrium")
plt.xlabel("$T$ [K]")
plt.ylabel("$D$ [Angstrom$^2$/ps]")
plt.show()

# cmiwiwwwww semangat guysssss..... nih script pake aja yaaa
# ntarrr tinggal run ajaa