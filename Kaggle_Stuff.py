def least_difference(a , b, c):
    """
    Return the smalles difference between any two numbers
    among a, b, c

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

#help(least_difference)

#print(least_difference(1, 10, 100))
help(abs)