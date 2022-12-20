from operator import mul
from functools import reduce
from factorial_check_input_value import checkInputValue


@checkInputValue
def factorial(number):
    return reduce(mul, range(1, number + 1), 1)
