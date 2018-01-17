

def twenty_seventeen():
    """Come up with the most creative expression that evaluates to 2017,
    using only numbers and the +, *, and - operators.

    >>> twenty_seventeen()
    2017
    """
    return ( \
           1+1+1+1+1+1+1+              1+ \
           1+                          1+ \
           1+                          1+ \
           1+             1+1+1+1+1+   1+ \
           1+             1+      1+   1+ \
           1+             1+      1+   1+ \
           1+             1+1+1+1+1+   1+ \
           1+1+1+1+1+1+1+         1+   1  ) * 0xC * 0xA * 0x1                                                    - 3143




print(twenty_seventeen())


