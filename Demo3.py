import numpy as np
from sympy.plotting import plot3d
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from sympy import *

from APP import Curve,s

r1=Curve(cos(s),sin(s),s)
l=2
r2=Curve(r1.x+l*(r1.frenet['n'][0]),r1.y+l*(r1.frenet['n'][1]),r1.z+l*(r1.frenet['n'][2]))
a=-10
b=10
fig = plt.figure(figsize = (20,20))
ax1 = fig.add_subplot(2,2,1,projection = "3d")
r1.plot(r1.r,a,b,ax1,'r1')
r2.plot(r2.r,a,b,ax1,'r2',linewidth=2)
ax2 = fig.add_subplot(2,2,2,projection = "3d")
r1.plot(r1.frenet['t'],a,b,ax2,'t1','b')
r2.plot(r2.frenet['t'],a,b,ax2,'t2','b',2)
ax3 = fig.add_subplot(2,2,3,projection = "3d")
r1.plot(r1.frenet['n'],a,b,ax3,'n1','r')
r2.plot(r2.frenet['n'],a,b,ax3,'n2','r',2)
ax4 = fig.add_subplot(2,2,4,projection = "3d")
r1.plot(r1.frenet['b'],a,b,ax4,'b1','c')
r2.plot(r2.frenet['b'],a,b,ax4,'b2','c',2)
plt.show()