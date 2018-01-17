HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [int(x**(0.5)) for x in s if x**(0.5) % 1 == 0]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        count = 3
        last, secondLast, thirdLast = 3, 2, 1
        while count < n:
            last, secondLast, thirdLast = last + secondLast * 2 + thirdLast * 3, last, secondLast
            count += 1
        return last

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # switch direction
    def switchDirection(number):
        return str(7) in list(str(number)) or number % 7 == 0

    # function for repeat calls
    def repeat(f, args, x):
        if x == 0:
            return args
        else:
            return repeat(f, f(args), x - 1)


    # pingpong(arr) => pingpong(arr + 1) # count is 1 higher
    # params: direction (1 or -1), count(k index), val
    # taken in as [direction, count, val]

    def pingPongHelper(arr):
        return [-arr[0] if switchDirection(arr[1]) else arr[0], arr[1] + 1, arr[2] - arr[0] if switchDirection(arr[1]) else arr[2] + arr[0]]

    def repeatHelper(x):
        if x == 1:
            return 1
        else:
            return repeat(pingPongHelper, [1, 1, 1], x - 1)[2]

    return repeatHelper(n)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"

    # greatest multiple of 2 less than or equal to x
    def greatestTwoMultipleLEQ(x):
        val = 1
        while (val * 2 <= x):
            val = val * 2
        return val

    verbose = True

    def count_change_helper(amt, maxVal):
        if verbose:
            print("calling: ", str(amt), str(maxVal))
        if maxVal == 0:
            if verbose:
                print(str(amt) + ", " + str(maxVal) + " returned 0")
            return 0
        elif amt == 0 or amt == 1:
            if verbose:
                print(str(amt) + ", " + str(maxVal) + " returned 1")
            return 1
        elif maxVal == 1:
            if verbose:
                print(str(amt) + ", " + str(maxVal) + " returned 1")
            return 1
        elif maxVal > amt:
            return count_change_helper(amt, maxVal // 2)
        else:
            return count_change_helper(amt, maxVal // 2) \
                + count_change_helper(amt - maxVal, maxVal)

    return count_change_helper(amount, greatestTwoMultipleLEQ(amount))






###################
# Extra Questions #
###################

# from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
