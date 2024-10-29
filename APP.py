
import numpy as np
from sympy.plotting import plot3d
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from sympy import *

s=symbols('s')

class Curve:
    #curve in E3
    def __init__(self,x=s,y=0,z=0):
        self.r=[x,y,z]
        self.x=x
        self.y=y
        self.z=z
        
        #Frenet frame
        t0=[f.diff(s) for f in self.r]
        ts=simplify(sqrt(sum([f**2 for f in t0])))
        t=[f/ts for f in t0]
        dt=[(f.diff(s))/ts for f in t]
        kappa=simplify(sqrt(sum([f**2 for f in dt])))
        n=[f/kappa for f in dt]
        b=self.wedge(t,n)
        tau=-simplify(((b[0]).diff(s))/(n[0]*ts))
        
        #curvature and torsion
        self.frenet={'t':t,'n':n,'b':b}
        self.nums={'kappa':kappa,'tau':tau}
    
    def wedge(self,x,y) ->list:
        return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
        
    def plot(self,x,sup,inf,ax,legend='',color='k',linewidth=1):
        s0=np.linspace(sup,inf,int(10*(inf-sup)))
        res=lambdify(s,x)(s0)
        ax.plot(res[0],res[1],res[2],label=legend,color=color,linewidth=linewidth)
        ax.legend()
