"""
Last Name: McConnell
First Name: Louie
Student ID number: 3032735110
CalCentral email: louie.mc@berkeley.edu
Discussion Section: Online 11-12:30pm
All the work on this exam is my own (please initial): LM

For each of the expressions in the table below, write the output displayed
by the interactive Python interpreter when the expression is evaluated. The
output may have multiple lines. If an error occurs, write "Error", but include
all output displayed before the error. if a function value is displayed, write
"Function".
The first two rows have been provided as examples.
Recall: The interactive interpreter displays the value of a successfully
evaluated expression, unless it is None.
Assume that you have started python3 and executed the following statements:
"""

from operator import mul

x = 3

def square(x):
    return mul(x, mul(x, 1))

def debug(x):
    x = x + 1
    return print(square(x))

"""
>>> pow(2, 3)
8
>>> print(4, 5) + 1
4 5
Error
>>> 25 or (5 / 0)
Error

>>> square(2) + square(x)
13

>>> print(square(3))
9

>>> debug(x)
16    # x == 4
None

>>> print(debug(2))
9
None

>>> debug(debug(x))
25
Error    # debug(None) (can’t run x = x + 1 on None)

"""
