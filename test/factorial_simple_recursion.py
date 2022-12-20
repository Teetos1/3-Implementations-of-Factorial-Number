from factorial_check_input_value import checkInputValue


@checkInputValue
def factorial(number):
    return 1 if number == 0 else number * factorial(number - 1)
