# Standard Deviation Calculator

  This is a standard deviation calculator for a sample set of numbers. The program should print the mean, variance, and standard deviation of the set of numbers entered by the user. This program is called `stdev_calc.py` and should be created with `new_py.py -a`. The user should enter multiple numbers seperated by a single space when running the program. If the user only enters one value, the program should die with a message saying "You need to enter more than one number." The code should first calculate the mean, then variance, and then standard deviation.
  
  Here is a helpful article with the equation as well as "psuedo code" written under "The Process" section: [How to Calculate a Sample Standard Deviation](https://www.thoughtco.com/calculate-a-sample-standard-deviation-3126345)
  
## Expected Behavior
```
$ ./stdev_calc.py
usage: stdev_calc.py [-h] int [int ...]
stdev_calc.py: error: the following arguments are required: int
```
```
$ ./stdev_calc.py -h
usage: stdev_calc.py [-h] int [int ...]

Standard Deviation Calculator Help

positional arguments:
  int         Enter number(s) with spaces between

optional arguments:
  -h, --help  show this help message and exit
```
```
$ ./stdev_calc.py 6
You need to enter more than one number.
```
```
$ ./stdev_calc.py 6 4 14 22
The Mean is: 11.5
The Variance is: 67.66666666666667
The Standard Deviation is: 8.225975119502044
```

## Test Suite
```
$ make test
pytest -v test.py
=============================================== test session starts ===============================================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- /rsgrps/bh_class/conda/bin/python
cachedir: .pytest_cache
rootdir: /home/u28/shelbeezy/STDEVCalculator, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
collected 4 items

test.py::test_usage PASSED                                                                                  [ 25%]
test.py::test_one PASSED                                                                                    [ 50%]
test.py::test_two PASSED                                                                                    [ 75%]
test.py::test_bad PASSED                                                                                    [100%]

============================================ 4 passed in 0.39 seconds =============================================
```

## Contact Information

Shelby Nelson
shelbeezy@email.arizona.edu
