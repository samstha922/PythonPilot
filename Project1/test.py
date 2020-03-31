import math
import matplotlib.pyplot as plt

def f(x):
    return 3*x+4
print (f(5))

def quadratic(x):
    g = 1-(x-1)**2
    return g
a=quadratic(5)
for a in (0,0.5,1,1.5,2):
    print("quadratic = {}".format(quadratic(a)))
def cubic (x):
    cub=x*(x-1)*(x-2)
    return cub
for v in range(0,21,1):
    print("v={}, quadratic = {:5.3f}, cubic = {:7.3f}". format(v/10, quadratic(v/10), cubic(v/10)))
def line(x):
    y=x
    return y
def sine_wave(x):
    s=math.sin(x*math.pi/2 *x )
    return s
#Challenge 5
lst_x = [0,0.5,1,1.5,2]
lst_y = [sine_wave(x) for x in lst_x]
plt.plot(lst_x, lst_y, label= "sine_wave", marker = 'x')
plt.legend()
plt.show()


