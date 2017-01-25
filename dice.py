# Exercise 1 - Quantum Dice
# From http://pyquil.readthedocs.io/en/latest/getting_started.html#exercise-1-quantum-dice
# Author: Aaron Vontell
# Written on Jan 24, 2017

from pyquil.quil import Program
from pyquil.gates import *
import pyquil.forest as forest
import math

def throw_octahedral_die():
    # return the result of throwing an 8 sided die, an int between 1 and 8, by running a quantum program
    
    qvm = forest.Connection()
    
    # Create a state that will be our source of "randomness"
    dice_prog = Program().inst(H(0), H(1), H(2))
    
    # Measure to get random bits
    dice_prog.measure(0, 0)
    dice_prog.measure(1, 1)
    dice_prog.measure(2, 2)
    
    # Get the result by running on a QVM
    bit_result = qvm.run(dice_prog, [0, 1, 2])
    bit_string = "".join(str(bit) for bit in bit_result[0])
    roll_result = int(bit_string, 2) + 1
    
    return roll_result

def throw_polyhedral_die(num_sides):
    # return the result of throwing a num_sides sided die by running a quantum program
    # Using the "throw out" method
    
    qvm = forest.Connection()
    
    # Calculate the number of qubits we will need
    num_bits = int(math.ceil(math.log(num_sides, 2)))
    
    # Create the source of randomness, and measure it
    dice_prog = Program()
    for i in range(num_bits):
        dice_prog.inst(H(i))
        dice_prog.measure(i, i)
    
    # Run this program on the QVM
    bit_result = qvm.run(dice_prog, range(num_bits))
    bit_string = "".join(str(bit) for bit in bit_result[0])
    roll_result = int(bit_string, 2) + 1
    
    # If this is above our desired number of sides, try again
    if roll_result > num_sides:
        return throw_polyhedral_die(num_sides) # We can make this memory efficient by passing the already constructed program
    else:
        return roll_result
      
print throw_octahedral_die()