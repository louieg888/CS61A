class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()


    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __len__(self):
        return 1 + len(self.rest)

    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1 2 3 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """

    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    else:
        # swapping locations
        firstLink = lnk
        secondLink = lnk.rest
        # swapping values
        firstLink.first, secondLink.first = secondLink.first, firstLink.first

        # recurse
        flip_two(secondLink.rest)

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> len(unique)
    2
    >>> len(lnk)
    2
    """

    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    else:
        if lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
            remove_duplicates(lnk)
            return lnk
        else:
            remove_duplicates(lnk.rest)
            return lnk

def reverse(lnk):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> r = reverse(a)
    >>> r.first
    3
    >>> r.rest.first
    2
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk

    restRev = reverse(lnk.rest)
    temp = lnk.rest
    lnk.rest = lnk.rest.rest
    temp.rest = lnk
    return restRev

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    nums = []

    noListEmpty = lambda: all([lst is not Link.empty for lst in lst_of_lnks])
    while noListEmpty():
        values = [link.first for link in lst_of_lnks]

        newVal = 1
        for val in values:
            newVal *= val

        nums.append(newVal)

        for i in range(len(lst_of_lnks)):
            lst_of_lnks[i] = lst_of_lnks[i].rest

    def listToLink(lst):
        if len(lst) == 0:
            return Link.empty
        else:
            return Link(lst[0], listToLink(lst[1:]))

    return listToLink(nums)

def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """

    return [lst[i] * i for i in range(len(lst)) if i % 2 == 0]

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    less = [elem for elem in lst if elem < pivot]
    greater = [elem for elem in lst if elem > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

def quicksort_link(link):
    if link is Link.empty or link.rest is Link.empty:
        return link
    pivot, link  = link, link.rest
    less, greater = Link.empty, Link.empty
    while link is not Link.empty:
        curr, rest = link, link.rest
        if curr.first < pivot.first:
            less, link.rest = extend_links(less, curr), Link.empty
        else:
            greater, link.rest = extend_links(greater, curr), Link.empty
        link = rest
    less = quicksort_link(less)
    greater = quicksort_link(greater)
    pivot.rest = greater
    return extend_links(less, pivot)

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)
    elif len(lst) == 3:
        return max(lst[0] * lst[2], lst[1])
    else:
        return max(lst[0] * max_product(lst[2:]), lst[1] * max_product(lst[3:]))

def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if is_leaf(tree):
        return tree.label
    args = [eval_tree(branch) for branch in branches(tree)]
    if label(tree) == '+':
        return sum(args)
    else: # label(tree) == '*'
        return prod(args)

def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ... Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while not all([y == [] for y in x]):
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)

def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(branch, new_f) for branch in t.branches]
    return t






