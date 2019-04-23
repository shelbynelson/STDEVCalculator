#!/usr/bin/env python3
"""tests for stdev_calc.py"""

import re
import os
import sys
from subprocess import getstatusoutput, getoutput

prg = './stdev_calc.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    rv, out = getstatusoutput('{} {}'.format(prg, '-h'))
    assert rv == 0
    assert re.match("usage", out, re.IGNORECASE)

# --------------------------------------------------
def test_one():
    expected = ('The Mean is: 11.5\nThe Variance is: 67.66666666666667\nThe Standard Deviation is: 8.225975119502044')

    rv, out = getstatusoutput('{} 6 4 14 22'.format(prg))
    assert rv == 0
    assert out == expected

# --------------------------------------------------
def test_two():
    expected = ('The Mean is: 9.25\nThe Variance is: 50.916666666666664\nThe Standard Deviation is: 7.135591542869215')

    rv, out = getstatusoutput('{} 10 3 5 19'.format(prg))
    assert rv == 0
    assert out == expected


# -------------------------------------------------
def test_bad():
    expected = ('You need to enter more than one number.')

    rv, out = getstatusoutput('{} 6'.format(prg))
    assert rv == 1
    assert out == expected

