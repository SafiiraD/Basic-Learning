from cProfile import label
from multiprocessing.synchronize import Lock
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,100,0.001)
y = np.sin(x)
plt.scatter(x,y)
plt.plot(x, 'cyan')
plt.plot(y, 'pink')
plt.title('Grafik sin(x)')
plt.xlabel('tetha (0-100)')
plt.ylabel('sin (x)')
# geser si legend biar ga bingung :v
plt.figure(1)
xy=plt.subplot(111)
plt.plot(x, label="Nilai X")
plt.plot(y, label="sin (x)")
box=xy.get_position()
plt.legend()
plt.text(20000,10, 'Grafik fungsi sin(x)')
#Kalo mau axis tambahin aja gapapa
 # plt.plot(xmin,xmax,ymin,ymax)
plt.show()