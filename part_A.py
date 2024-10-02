"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

#WE IMPORT THE LIBRARIES
import numpy as np

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    # WE CALCULATE THE LENGTH OF X

    count = 0

    while x[count:]:
        count = count+1

    N = count 


    # WE CALCULATE THE SUM OF ALL TERMS AND CALCULATE THE MEAN OF X

    count = N-1
    sumx = 0

    while count >= 0:
        sumx = sumx + x[count]
        count = count-1

    meanx = (1/N) * sumx


    # WE COMPUTE THE SUM OF THE SQUARES AND THEN IT'S MEAN (S)

    count = N-1
    sumx2 = 0

    while count >= 0:
        sumx2 = sumx2 + ((x[count])**2)
        count = count-1

    S = (1/N) * sumx2


    # WE COMPUTE THE VARIANCE

    var1 = meanx**2
    variance = S - var1

    # WE COMPUTE THE STANDARD DEVIATION

    sd = variance**(1/2)
    
    return sd
    

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    # WE CALCULATE THE LENGTH AND THE SUM OF ALL TERMS, ALLOWING US TO COMPUTE THE MEAN OF X

    N=len(x)

    meanx = (1/N) * np.sum(x)

    # WE COMPUTE "S" (THE MEAN OF THE SQUARES)

    S = (1/N) * np.sum(x**2)

    # WE COMPUTE THE VARIANCE

    var1 = meanx**2
    variance = S - var1

    # WE COMPUTE THE STANDARD DEVIATION

    sd = variance**(1/2)
    
    return sd