import numpy as np
from sympy.plotting import plot3d
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from sympy import *

from APP import Curve,s
        
r1=Curve(cos(s),sin(s),s)
a=-10
b=10
fig = plt.figure(figsize = (20,20))
ax1 = fig.add_subplot(2,2,1,projection = "3d")
r1.plot(r1.r,a,b,ax1,'r')
ax2 = fig.add_subplot(2,2,2,projection = "3d")
r1.plot(r1.frenet['t'],a,b,ax2,'t','b')
ax3 = fig.add_subplot(2,2,3,projection = "3d")
r1.plot(r1.frenet['n'],a,b,ax3,'n','r')
ax4 = fig.add_subplot(2,2,4,projection = "3d")
r1.plot(r1.frenet['b'],a,b,ax4,'b','c')
plt.show()

