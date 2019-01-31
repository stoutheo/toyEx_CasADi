#!/usr/bin/env

from sys import path

# temp intallation folder of CasADi (pre-compiled version)
path.append(r"/home/theo/software/tools/CasADi/test/casadi-linux-py27-58aa427")
from casadi import *

#########################
     # SX
#########################

# scalar variable
x = MX.sym('x')

# 1x5 vector
y = SX.sym('y', 5)

# 4x2 matrix
Z = SX.sym('Z', 4 , 2)


f = x**2 + 10
f = sqrt(f)

print('f:',f)

#########################
     # DM
#########################

B1 = SX.zeros(4,5) # A dense 4-by-5 empty matrix with all zeros
B2 = SX(4,5)       # A sparse 4-by-5 empty matrix with all zeros
B4 = SX.eye(4)     # A sparse 4-by-4 matrix with ones on the diagonal

print "\n","actual zeros: \n", B1, "\n"

print "structural zeros:", B2


C = DM(2,3)
C_dense = C.full()

from numpy import array
C_dense = array(C) # equivalent
C_sparse = C.sparse()

from scipy.sparse import csc_matrix
C_sparse = csc_matrix(C) # equivalent


#########################
     # MX
#########################

x = SX.sym('x',2,2)
y = SX.sym('y')
f = 3*x + y
print(f)
print "Shape is ", f.shape


x = MX.sym('x',2,2)
y = MX.sym('y')
f = 3*x + y
print(f)
print "Shape is ", f.shape

x = MX.sym('x',2,2)
print(x[1,0])





print(SX.sym('x',Sparsity.lower(3)))

print "MX"
print(MX.sym('x',Sparsity.lower(3)))

print(DM(Sparsity.lower(3)))



# Getting and setting elements in matrices

M = SX([[3,7],[4,5]])
print(M[0,:])
M[0,:] = 1
print(M)
print(M[0,:])

M = SX([[3,7],[4,5]])
print(M[0,:][0,0])
M[0,:][0,0] = 1
print(M)



M = diag(SX([3,4,5,6]))
print(M)

print(M[:,1])
print(M[1:,1:4:2])
#
# M = SX([[3,7,8,9],[4,5,6,1]])
# print(M)
# print(M[0,[0,3]], M[[5,-6]])
print type(M.sparsity())

A = MX.sym('A',3,3)
b = MX.sym('b',3)
print(solve(A,b))

#################################
# Function objects
#################################
x = SX.sym('x',2)
y = SX.sym('y')
f = Function('Kliasd',[x,y], [x,sin(y)*x])
print(f)


x = MX.sym('x',2)
y = MX.sym('y')
f = Function('f',[x,y],[x,sin(y)*x],['x','y'],['r','q'])
print(f)

r0, q0 = f(1.1,3.3)
print('r0:',r0)
print('q0:',q0)


########################################################################
#      Root finding
########################################################################

nz = 1;
nx = 1;
z = SX.sym('x',nz)
x = SX.sym('x',nx)
g0 = sin(x+z)
g1 = cos(x-z)
g = Function('g',[z,x],[g0,g1], ['x','y'],['r','q'])
G = rootfinder('G','newton',g)
print(G)

r0 , q0 = G(5,2)
print r0, q0
########################################################################
#  Initial-value problems and sensitivity analysis
########################################################################
x = SX.sym('x');
z = SX.sym('z');
p = SX.sym('p')

dae = {'x':x, 'z':z, 'p':p, 'ode':z+p, 'alg':z*cos(z)-x}
F = integrator('F', 'idas', dae)
print(F)

# Integrating this DAE from 0 to 1 with x(0)=0, p=0.1 and using the guess z(0)=0
r = F(x0=0, z0=0, p=0.1)
print(r['xf'])



########################################################################
#  Nonlinear programming
########################################################################

# Rosenbrock problem

l = SX.sym('l');
y = SX.sym('y');
z = SX.sym('z');

nlp = {'x':vertcat(l,y,z),
       'f':l**2+100*z**2,
       'g':z+(1-l)**2-y}

S = nlpsol('S', 'ipopt', nlp)
print(S)

r = S(x0=[2.5,3.0,0.75], lbg=0, ubg=0)
x_opt = r['x']
print('x_opt: ', x_opt)



N = 4
X = MX.sym("X",1,N)
print(f)
###
