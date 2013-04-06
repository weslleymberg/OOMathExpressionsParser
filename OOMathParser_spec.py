import unittest
from should_dsl import *

from OOMathParser import *

class TestMathExpression(unittest.TestCase):

    def setUp(self):
        self.an_expression = Expression()

    def it_should_raise_non_implemented_exception_for_its_methods(self):
        self.an_expression.evaluate |should| throw(NotImplementedError)


class TestLiteral(unittest.TestCase):

    def setUp(self):
        self.a_literal = Literal(2.0)

    def test_it_should_return_its_value(self):
        self.a_literal.evaluate() |should| equal_to(2)

    def test_it_should_accept_only_integer_or_float_parameters(self):
        (Literal, None) |should| throw(ValueError, message='Parameter must be float!')
        (Literal, "string") |should| throw(ValueError, message='Parameter must be float!')
        (Literal, 1) |should| throw(ValueError, message='Parameter must be float!')


class TestCompoundExpression(unittest.TestCase):

    def setUp(self):
        self.a_literal = Literal(2.0)
        self.another_literal = Literal(3.0)
        self.a_compound_expression = CompoundExpression(self.a_literal, self.another_literal)

    def test_it_should_contain_a_left_expression(self):
        self.a_compound_expression.left_expression |should| be(self.a_literal)

    def test_it_should_contain_a_right_expression(self):
        self.a_compound_expression.right_expression |should| be(self.another_literal)

    def test_it_should_not_implements_superclass_methods(self):
        self.a_compound_expression.evaluate |should| throw(NotImplementedError)

    def test_it_should_accept_only_arguments_of_the_type_expression(self):
        (CompoundExpression, "an expression", "another expression") |should| throw(ValueError)
        (CompoundExpression, 1, 2) |should| throw(ValueError)


class TestSum(unittest.TestCase):

    def setUp(self):
        self.an_integer_literal = Literal(2.0)
        self.another_integer_literal = Literal(5.0)
        self.a_sum_expression = Sum(self.an_integer_literal, self.another_integer_literal)

    def test_it_should_assign_its_parameters(self):
        self.a_sum_expression.left_expression |should| be(self.an_integer_literal)
        self.a_sum_expression.right_expression |should| be(self.another_integer_literal)

    def test_it_should_sum_the_two_expressions(self):
        self.a_sum_expression.evaluate() |should| equal_to(7.0)


class TestSubtract(unittest.TestCase):

    def setUp(self):
        self.a_literal = Literal(2.0)
        self.another_literal = Literal(5.0)
        self.a_subtract_expression = Subtract(self.a_literal, self.another_literal)

    def test_it_should_assign_its_parameters(self):
        self.a_subtract_expression.left_expression |should| be(self.a_literal)
        self.a_subtract_expression.right_expression |should| be(self.another_literal)

    def test_it_should_subtract_the_two_expressions(self):
        self.a_subtract_expression.evaluate() |should| equal_to(-3)


class TestMultiply(unittest.TestCase):

    def setUp(self):
        self.a_literal = Literal(2.0)
        self.another_literal = Literal(5.0)
        self.a_multiply_expression = Multiply(self.a_literal, self.another_literal)

    def test_it_should_assign_its_parameters(self):
        self.a_multiply_expression.left_expression |should| be(self.a_literal)
        self.a_multiply_expression.right_expression |should| be(self.another_literal)

    def test_it_should_multiply_the_two_expressions(self):
        self.a_multiply_expression.evaluate() |should| equal_to(10)


class TestDivide(unittest.TestCase):

    def setUp(self):
        self.a_literal = Literal(10.0)
        self.another_literal = Literal(5.0)
        self.a_divide_expression = Divide(self.a_literal, self.another_literal)

    def test_it_should_assign_its_parameters(self):
        self.a_divide_expression.left_expression |should| be(self.a_literal)
        self.a_divide_expression.right_expression |should| be(self.another_literal)

    def test_it_should_divide_the_two_expressions(self):
        self.a_divide_expression.evaluate() |should| equal_to(2)
