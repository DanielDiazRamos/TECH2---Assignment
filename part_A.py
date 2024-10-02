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

    var1 = np.sum(meanx**2)
    variance = S - var1

    # WE COMPUTE THE STANDARD DEVIATION

    sd = variance**(1/2)