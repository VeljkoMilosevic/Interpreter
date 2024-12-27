from src.adding import Addition
from src.number import Number

expression = "1+2+5"

while len(expression) != 1:
    if ex == "+":
        number1 = Number()
        number1.set_value(expression[index-1])
        number2 = Number()
        number2.set_value(expression[index+1])
        addition = Addition()
        print(addition.evaluate(number1, number2))
        expression = expression[2:len(expression)]