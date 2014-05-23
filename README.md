OOMathExpressionsParser
=======================

An interpreter for math expressions.

Example:

    In [3]: e = Expression('10-4+5')
    In [4]: e.evaluate()
    Out[4]: 11.0

    In [2]: e = Expression('10/2')
    In [3]: e.evaluate()
    Out[3]: 5.0


Note:
- Math operators do not have priority yet.
- Parenthesis are not being interpreted yet.
- Operations with negative numbers (e.g. -1+2) do not work well.
