import os
import sys


file = 'blackscholes.cpp'

os.system("rm ../tempscripts/{}".format(file))
os.system("cp ../scripts/{} ../tempscripts/".format(file))
os.system("make clean")
