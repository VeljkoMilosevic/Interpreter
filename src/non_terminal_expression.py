from abc import abstractmethod
from expression import Expression


class NonTerminalExpression(Expression):
    @abstractmethod
    def evaluate(self):
        pass
