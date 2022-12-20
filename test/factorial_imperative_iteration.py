from factorial_check_input_value import checkInputValue


@checkInputValue
def factorial(number):
    product = 1

    for numbers in range(1, number + 1):
        product *= numbers

    return product
