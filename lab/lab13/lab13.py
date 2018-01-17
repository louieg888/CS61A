## Generators

def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def ints_to(n):
    ...     for i in range(1, n + 1):
    ...          yield i
    ...
    >>> def ints_to_5():
    ...     for item in ints_to(5):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(ints_to_5):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    1
    Next Generator:
    1
    2
    Next Generator:
    1
    2
    3
    Next Generator:
    1
    2
    3
    4
    Next Generator:
    1
    2
    3
    4
    5
    """
    "*** YOUR CODE HERE ***"
    def subgen(i):
        count = 0
        for element in g():
            if count < i:
                yield element
                count += 1
            else:
                break

    k = 1

    for item in g():
        yield subgen(k)
        k+=1

def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return
    "*** YOUR CODE HERE ***"
    # a, b
    # b, a

    # a, b, c
    # b, a, c
    # c, a, b
    # c, b, a
    # a, c, b
    # b, c, a

    # c, a, b
    # a, c, b
    # a, b, c
    # c, b, a
    # b, c, a
    # b, a, c

    for perm in permutations(lst[1:]):
        for i in range(len(lst)):
            yield perm[:i] + [lst[0]] + perm[i:]

