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

    def __init__(self, left_expression, right_expression):
        super(Sum, self).__init__(left_expression, right_expression)

    def evaluate(self):
        return self.left_expression.evaluate() + self.right_expression.evaluate()


class Subtract(_CompoundExpression):

    def __init__(self, left_expression, right_expression):
        super(Subtract, self).__init__(left_expression, right_expression)

    def evaluate(self):
        return self.left_expression.evaluate() - self.right_expression.evaluate()


class Multiply(_CompoundExpression):

    def __init__(self, left_expression, right_expression):
        super(Multiply, self).__init__(left_expression, right_expression)

    def evaluate(self):
        return self.left_expression.evaluate() * self.right_expression.evaluate()


class Divide(_CompoundExpression):

    def __init__(self, left_expression, right_expression):
        super(Divide, self).__init__(left_expression, right_expression)

    def evaluate(self):
        return self.left_expression.evaluate() / self.right_expression.evaluate()
