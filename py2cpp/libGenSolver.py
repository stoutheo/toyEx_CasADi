from sys import path
import numpy as np

# temp intallation folder of CasADi (pre-compiled version)
path.append(r"/home/theo/software/tools/CasADi/test/casadi-linux-py27-58aa427")

from casadi import *

from os import system

# source : https://github.com/casadi/casadi/blob/master/docs/examples/cplusplus/nlp_codegen.cpp
# c++ example modified into python

# Optimization variables
x=SX.sym("x",2)
p=SX.sym("p")

# Objective
f = x[0]*x[0] + x[1]*x[1];

# Constraints
g = x[0]+x[1]-p;

# Create an NLP solver instance
nlp = {'x':x, 'p':p, 'f':f, 'g':g}
S = nlpsol('S', 'ipopt', nlp)

#  Generate C code for the NLP solver
S.generate_dependencies("libSolver.c");

#  compile it
system("gcc -fPIC -shared -O3 libSolver.c -o libSolver.so")

# to move files to correct location
import shutil

# move it to the c_code folder
shutil.move("libSolver.c", "c_code/libSolver.c")

# move it to the lib folder
shutil.move("libSolver.so", "lib/libSolver.so")
#
