#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-04-22
Purpose: Calculates the standard deviation of a sample set of numbers
"""

import argparse
import sys
import os
from math import sqrt

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Standard Deviation Calculator Help',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'value', metavar='int', type=int, help='Enter number(s) with spaces between', nargs='+')

    return parser.parse_args()

# --------------------------------------------------
def warn(msg):
    print(msg, file=sys.stderr)

# -------------------------------------------------
def die(msg='Something bad happened'):
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    num_vals = args.value
    length = len(num_vals)
    sum_ = 0
    sq_sum = 0
    
    if length == 1:
        die('You need to enter more than one number.')

   
    """Calculates the Mean"""       
    for val in range(length):
        sum_ += num_vals[val]
    mean= sum_/length

    """Calculates Variance and then Standard Deviation"""
    for val in range(length):
       sq_sum += pow((num_vals[val]-mean),2)
    var = sq_sum/(length-1)
    stdev = sqrt(var)
    
    print('The Mean is: {}\nThe Variance is: {}\nThe Standard Deviation is: {}'.format(mean, var, stdev))
       
       

# --------------------------------------------------
if __name__ == '__main__':
    main()
