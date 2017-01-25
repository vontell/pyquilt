# Exercise 2 - Controlled Gates
# http://pyquil.readthedocs.io/en/latest/getting_started.html#exercise-2-controlled-gates
# Author: Aaron Vontell
# Written on Jan 24, 2017

from pyquil.quil import Program
from pyquil.gates import *
import pyquil.forest as forest
import numpy as np

def controlled(U):
    # Returns a controlled variant of U
    # Is there a more efficient and universal way to do this...
    return np.array([[1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, U[0][0], U[0][1]],
                    [0.0, 0.0, U[1][0], U[1][1]]])

def def_cont_Y():
    # Defines a controlled Y gate in Quil
  
    qvm = forest.Connection()
  
    # Create the controlled Y gate
    y_gate_matrix = np.array(([0.0, -1.0j], [1.0j, 0.0]))
    cont_y = controlled(y_gate_matrix)
    p = Program()
    p.defgate("CONT-Y", cont_y)
  
    # Find the wavefunction when applying this gate to qubit 1 controlled by qubit 0
    p.inst(("CONT-Y", 0, 1))
    return qvm.wavefunction(p)
  
print def_cont_Y()