from sys import path

# temp intallation folder of CasADi (pre-compiled version)
path.append(r"/home/theo/software/tools/CasADi/test/casadi-linux-py27-58aa427")

import casadi as ca
import numpy as np

xgrid = np.linspace(1,6,6)
V = [-1,-1,-2,-3,0,2]
lut = ca.interpolant('LUT','bspline',[xgrid],V)
print(lut(2.5))

#############################################
xgrid = np.linspace(-5,5,11)
ygrid = np.linspace(-4,4,9)
X,Y = np.meshgrid(xgrid,ygrid,indexing='ij')
R = np.sqrt(5*X**2 + Y**2)+ 1
data = np.sin(R)/R
data_flat = data.ravel(order='F')

print data.shape

dataXY = np.array([X,Y])
dataXY_flat = dataXY.ravel(order='F')

print dataXY_flat.shape
# lut = ca.interpolant('name','bspline',[xgrid,ygrid],data_flat)
lut = ca.interpolant('name','bspline',data_flat, [X,Y])

print(lut([0.5,1]))
