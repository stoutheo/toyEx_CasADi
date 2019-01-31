from sys import path
import numpy as np

# temp intallation folder of CasADi (pre-compiled version)
path.append(r"/home/theo/software/tools/CasADi/test/casadi-linux-py27-58aa427")

from casadi import *

from os import system

# source : https://gist.github.com/jgillis/41abbe1c9f2f2736024bb1ecb33ee51c

x=SX.sym("x",4,1)
y=SX.sym("y")

z = vertcat(sin(x[0]*y),cos(x[1]*sqrt(y)-x[2]),x[3])

f = Function('f',[x,y],[z])

#  make the generator for storing all info as .so
cg = CodeGenerator('libExampleFun')
cg.add(f)
cg.add(f.forward(1))
cg.add(f.reverse(1))
cg.add(f.reverse(1).forward(1))
# generate c file
cg.generate()

#  compile it
system("gcc -fPIC -shared -O3 libExampleFun.c -o libExampleFun.so")

# if we wanted to load it in python
# f_ext = external("f","./code.so")

# to move files to correct location
import shutil

# move it to the c_code folder
shutil.move("libExampleFun.c", "c_code/libExampleFun.c")

# move it to the lib folder
shutil.move("libExampleFun.so", "lib/libExampleFun.so")
#
