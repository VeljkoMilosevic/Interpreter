from terminal_expression import TerminalExpression


class Number(TerminalExpression):
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def evaluate(self):
        return int(self.value)
