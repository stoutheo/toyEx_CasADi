import numpy as np

from sys import path

# temp intallation folder of CasADi (pre-compiled version)
path.append(r"/home/theo/software/tools/CasADi/test/casadi-linux-py27-58aa427")

from casadi import *

# state
x=SX.sym("x")

#control
u=SX.sym("u")

# fixed param
a = SX.sym("a")

# Create an integrator
ode = {"x":x,"p":vertcat(a,u),"ode": -a*x+u}
I = integrator("sys","cvodes",ode,{"tf":0.1})

# Simulate N steps
N = 100
sim = I.mapaccum("simulator",N)

# Initial state
X0 = 1.0
# Row vector of control signals
U = sin(DM(np.linspace(0,1,N))*N*5).T
# parameter
a = 2

# Simulate
out = sim(x0=X0,p=vertcat(repmat(a,1,N),U))


# Plot the states
import pylab
pylab.plot(out["xf"].T)
pylab.show()
