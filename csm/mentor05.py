def num_digits(n):
    """Takes in an positive integer and returns the number of
    digits.
    >>> num_digits(0)
    1
    >>> num_digits(1)
    1
    >>> num_digits(7)
    1
    >>> num_digits(1093)
    4
    """
    if n // 10 == 0:
        return 1
    else:
        return 1 + num_digits(n // 10)

def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n // 10 == 0:
        return True
    else:
        return n % 10 <= (n % 100 - n % 10) // 10 and is_sorted(n//10)

def mario_number(level):
    """
    Return the number of ways that mario can traverse the
    level where mario can either hop by one digit or two
    digits each turn a level is defined as being an integer
    where a 1 is something mario can step on and 0 is
    something mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """

    if level % 10 == 0:
        return 0
    elif level == 1:
        return 1
    else:
        return mario_number(level // 10) + mario_number(level // 100)

def make_change(n):
    """Write a function, make_change that takes in an
    integer amount, n, and returns the minimum number
    of coins we can use to make change for that n,
    using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
    2
    """
    if n < 1:
        return 0
    elif n < 3:
        return 1 + make_change(n - 1)
    elif n < 4:
        return min(1 + make_change(n-1), 1 + make_change(n-3))
    else:
        return min(1 + make_change(n-1), 1 + make_change(n-3), 1 + make_change(n-4))
