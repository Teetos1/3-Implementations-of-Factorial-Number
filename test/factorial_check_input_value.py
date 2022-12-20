def checkInputValue(func):
    def inner(number):
        if number < 0:
            raise ValueError("Number should be Zero or greater")
        return func(number)

    return inner
