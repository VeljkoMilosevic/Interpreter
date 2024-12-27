from abc import abstractmethod


class Expression:
    @abstractmethod
    def evaluate(self):
        pass

