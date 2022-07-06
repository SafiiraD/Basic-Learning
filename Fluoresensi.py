from scipy import stats
import matplotlib.pyplot as plt

#Fitting Kurva
x = [0,2,4,6,8,10, 12,14,16,18,20]
y = [2.1, 5.0, 9.0, 12.6, 17.3, 21.0, 24.7, 28.4, 31.0, 32.9, 33.9]
Konsentrasi = x
Intensitas = y
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
intensitas = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, intensitas)
plt.title('Fluoresensi')
plt.xlabel("Konsentrasi")
plt.ylabel("Intensitas")
plt.show()

#Print regresi
x = [0,2,4,6,8,10, 12,14,16,18,20]
y = [2.1, 5.0, 9.0, 12.6, 17.3, 21.0, 24.7, 28.4, 31.0, 32.9, 33.9]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
speed = myfunc(10)
print(speed)

