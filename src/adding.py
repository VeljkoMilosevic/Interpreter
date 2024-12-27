from non_terminal_expression import NonTerminalExpression
from number import Number


class Addition(NonTerminalExpression):
    def evaluate(self, left: Number, right: Number):
        return left.evaluate() + right.evaluate()
