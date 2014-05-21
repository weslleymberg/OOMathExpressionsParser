import unittest
from should_dsl import should

from OOMathParser import *

class TestLiteral(unittest.TestCase):

    def setUp(self):
        self.a_literal = Literal(2.0)

    def test_it_should_return_its_value(self):
        self.a_literal.evaluate() |should| equal_to(2)

    def test_it_should_accept_only_integer_or_float_parameters(self):
        (Literal, None) |should| throw(ValueError, message='Parameter must be float!')
        (Literal, "string") |should| throw(ValueError, message='Parameter must be float!')
        (Literal, 1) |should| throw(ValueError, message='Parameter must be float!')


class TestSum(unittest.TestCase):

    def setUp(self):
        self.an_integer_literal = Literal(2.0)
        self.another_integer_literal = Literal(5.0)
        self.a_sum_expression = Sum(self.an_integer_literal, self.another_integer_literal)

    def test_it_should_accept_only_arguments_of_the_type_expression(self):
        (Sum, "an expression", "another expression") |should| throw(ValueError)
        (Sum, 1, 2) |should| throw(ValueError)

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

    def test_it_should_accept_only_arguments_of_the_type_expression(self):
        (Subtract, "an expression", "another expression") |should| throw(ValueError)
        (Subtract, 1, 2) |should| throw(ValueError)

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

    def test_it_should_accept_only_arguments_of_the_type_expression(self):
        (Multiply, "an expression", "another expression") |should| throw(ValueError)
        (Multiply, 1, 2) |should| throw(ValueError)

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

    def test_it_should_accept_only_arguments_of_the_type_expression(self):
        (Divide, "an expression", "another expression") |should| throw(ValueError)
        (Divide, 1, 2) |should| throw(ValueError)

    def test_it_should_assign_its_parameters(self):
        self.a_divide_expression.left_expression |should| be(self.a_literal)
        self.a_divide_expression.right_expression |should| be(self.another_literal)

    def test_it_should_divide_the_two_expressions(self):
        self.a_divide_expression.evaluate() |should| equal_to(2)


class TestParse(unittest.TestCase):

    def test_it_should_evaluate_3_plus_2_equals_to_5(self):
        expression = Expression("3+2")
        expression.evaluate() |should| equal_to(5)

    def test_it_should_evaluate_1_plus_1_equals_to_2(self):
        expression = Expression("1 + 1")
        expression.evaluate() |should| equal_to(2)
