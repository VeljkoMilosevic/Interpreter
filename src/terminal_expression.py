from abc import abstractmethod
from expression import Expression


class TerminalExpression(Expression):
    @abstractmethod
    def evaluate(self):
        pass
