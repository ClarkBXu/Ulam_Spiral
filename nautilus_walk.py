# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:13:44 2022

@author: Clark Xu
"""

import numpy as np

def get_corners(s: int, verbose: bool = False):
    """
    Helper function to get corners of a square
    
    Input
    s - root of the lower left corner of the square
    verbose - bool for print corners to console
    
    Output
    out - list of ints containing [lower left corner, lower right corner, upper left corner, upper right corner]
    """
    # Initialize output
    out = []
    
    # Calculate and store corner
    corner = s**2
    out.append(corner)
    
    # Get side length of square
    offset = s - 1
    
    # Get corners
    for _ in range(3):
        corner -= offset
        out.append(corner)
    
    # Print output
    if verbose:
        print("Corners are",out)
    
    # Return output
    return out

def get_distance(corner1: int, corner2: int, point: int, anchor: int, verbose: bool = False):
    """
    Helper function to get Manhattan distance
    
    Input
    corner1 - int representing smaller corner of square
    corner2 - int representing larger corner of square
    point - int representing point on Nautilus Walk
    anchor - int representing the root of the lower left corner of square
    verbose - bool for print distance to console
    
    Output
    out - int representing Manhattan distance    
    """
    # Get axis 1 distance
    axis1 = (anchor - 1) / 2
    
    # Get side midpoint
    midpoint = (corner1+corner2)/2
    
    # Get axis 2 distance
    axis2 = abs(midpoint - point)
    
    # Get Manhattan distance
    distance = axis1 + axis2
    
    # Print output
    if verbose:
        print("Distance is",distance)
    
    # Return Manhattan distance
    return distance
    

def nautilus_walk(x: int, c: int = 1, verbose: bool = True):
    """
    Function for computing L1-norm (Manhattan) distance 
    between center c and integer x on the Ulam spiral
    
    Input
    x - int for entry on the Ulam spiral
    c - int for center of the Ulam spiral
    verbose - bool for print nautilus walk output to console
    
    Output
    distance - int for Manhattan distance between x and c on Ulam spiral
    """
    # Enforce args
    try:
        int(x)
        int(c)
        bool(verbose)
    except:
        return ValueError("Error reading args")
        
    # Enforce constraints on x, c
    if (x < 1) or (c < 1) or (x < c):
        return ValueError("Error with locating x, c on Ulam spiral")
    
    # Account for offset of x by c
    core = (x - (c - 1))
    
    # Get root of offset
    root = (core)**(.5)
    
    # Round up to nearest odd and get previous odd
    nearestOdd = (np.ceil(root) // 2) * 2 + 1
    previousOdd = nearestOdd - 2
    
    # Get square corners (ll = lower left, lr = lower right, ul = upper left, ur = upper right)
    [llCorner, lrCorner, ulCorner, urCorner] = get_corners(nearestOdd)
    
    # Compute L1-norm between x and c
    ## Lower side
    if (core <= llCorner) and (core > lrCorner):
        distance = get_distance(lrCorner,llCorner,core,nearestOdd)
    ## Left side
    elif (core <= lrCorner) and (core > ulCorner):
        distance = get_distance(ulCorner,lrCorner,core,nearestOdd)
    ## Upper side
    elif (core <= ulCorner) and (core > urCorner):
        distance = get_distance(urCorner,ulCorner,core,nearestOdd)
    ## Right side
    elif (core <= urCorner) and (core > previousOdd):
        distance = get_distance(previousOdd**2,urCorner,core,nearestOdd)
    
    # Print output
    if verbose:
        # Define output string
        output = "The Manhattan distance between {c} and {x} on the Nautilus Walk is {distance}"
        
        # Print output to console
        print(output.format(c=c,x=x,distance=int(distance)))
    
    # L1-norm distance is always an integer
    return int(distance)

def main():
    # Standard Test Cases
    print("Standard Test")
    assert nautilus_walk(1) == 0
    assert nautilus_walk(12) == 3
    assert nautilus_walk(23) == 2
    assert nautilus_walk(1024) == 31
    print("")
    
    # Diagonal Test Cases
    print("Diagonal Test")
    assert nautilus_walk(9) == 2
    assert nautilus_walk(25) == 4
    assert nautilus_walk(49) == 6
    assert nautilus_walk(81) == 8
    print("")
    
    # Edge Test Cases
    print("Edge Test")
    assert nautilus_walk(2) == 1
    assert nautilus_walk(3) == 2
    assert nautilus_walk(100000) == 173
    assert nautilus_walk(100000000) == 9999
    assert nautilus_walk(1,1,False) == 0
    assert nautilus_walk(2,2,False) == 0
    print("")
    
    # Error Test Cases
    print("Error Test")
    print(nautilus_walk("One"))
    print(nautilus_walk(1,"One"))
    print(nautilus_walk(-1))
    print(nautilus_walk(1,-1))
    print(nautilus_walk(1,5))
    print("")

if __name__ == "__main__":
    main()