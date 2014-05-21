import re

class _Expression(object):
    """
    This is an abstract class for every class
    that aims to implement a math expression;
    """

    def __new__(cls, *args, **kwargs):
        if cls is _Expression:
            raise TypeError("Expression class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)

    def evaluate(self):
        raise NotImplementedError('Should have implemented this!')


class Literal(_Expression):

    def __init__(self, value):
        if type(value) == float:
            self.value = value
        else:
            raise ValueError('Parameter must be float!')

    def evaluate(self):
        return self.value


class _CompoundExpression(_Expression):
    """
    This is an abstract class for compound expressions
    """

    def __new__(cls, *args, **kwargs):
        if cls is _CompoundExpression:
            raise TypeError("CompoundExpression class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)


    def __init__(self, left_expression, right_expression):
        if issubclass(left_expression.__class__, _Expression) and issubclass(right_expression.__class__, _Expression):
            self.left_expression = left_expression
            self.right_expression = right_expression
        else:
            raise ValueError('Parameters must be an Expression subclass instance!')


class Sum(_CompoundExpression):

    def evaluate(self):
        return self.left_expression.evaluate() + self.right_expression.evaluate()


class Subtract(_CompoundExpression):

    def evaluate(self):
        return self.left_expression.evaluate() - self.right_expression.evaluate()


class Multiply(_CompoundExpression):

    def evaluate(self):
        return self.left_expression.evaluate() * self.right_expression.evaluate()


class Divide(_CompoundExpression):

    def evaluate(self):
        return self.left_expression.evaluate() / self.right_expression.evaluate()


class Expression(_Expression):

    def __init__(self, expression):
        self.expression = expression
        self.operators = {'+': Sum, '-': Subtract, '*': Multiply, '/': Divide}

    def evaluate(self):
        symbols = re.split('([+\-\*/])', self.expression)
        print symbols
        left = self._convert_to_float(symbols[0])
        right = self._convert_to_float(symbols[2])
        operator = self.operators[symbols[1]](left, right)
        return operator.evaluate()

    def _convert_to_float(self, symbol):
        try:
            number = float(symbol)
        except ValueError:
            raise
        else:
            return Literal(number)
