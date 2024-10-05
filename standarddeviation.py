# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:25:34 2024

@author: dadir
"""
# WE IMPORT NUMPY AND OUR OWN LIBRARY

import part_A
import numpy as np


# WE CALCULATE THE RESULT USING THE LOOPS FUNCTION

x = [1, 2, 3, 4, 5]
print("Result with loops: ", part_A.std_loops(x))


# NOW WE CALCULATE THE RESULT USING THE FUNCTION WHICH USES BUILT-IN FUNCTIONS

x = [1, 2, 3, 4, 5]
print("Result with functions: ", part_A.std_builtin(x))


# WE FINALIZE BY TESTING NUMPY'S OWN STD FUNCTION

x = np.array([1, 2, 3, 4, 5])
print("Result with NP's std: ", np.std(x))


# ALL RESULTS ARE INDEED THE SAME