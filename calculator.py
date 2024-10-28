class InvalidArgumentError(Exception):
    pass


class UnknownOperationError(Exception):
    pass


class InvalidOperandError(Exception):
    pass


class Calculator:
    def __init__(self):
        self.operations = {}

    def add_method(self, operation, func):
        if not isinstance(operation, str) or not callable(func):
            raise InvalidArgumentError('INVALID_ARGUMENT')
        self.operations[operation] = func

    def calculate(self, expression):
        if not isinstance(expression, str):
            raise InvalidArgumentError('INVALID_ARGUMENT')

        parts = expression.split()
        if len(parts) != 3:
            raise InvalidOperandError('INVALID_OPERAND')

        a, operator, b = parts

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise InvalidOperandError('INVALID_OPERAND')

        if operator not in self.operations:
            raise UnknownOperationError('UNKNOWN_OPERATION')

        return self.operations[operator](a, b)


# Пример использования
calc = Calculator()
calc.add_method('+', lambda a, b: a + b)
calc.add_method('-', lambda a, b: a - b)
calc.add_method('*', lambda a, b: a * b)
calc.add_method('/', lambda a, b: a / b)

try:
    print(calc.calculate("12 + 4"))  # 16
    print(calc.calculate("3 * 5"))  # 15
    print(calc.calculate("10 - 2"))  # 8
    print(calc.calculate("2 / 0"))  # ZeroDivisionError
    print(calc.calculate("h - 10"))  # InvalidOperandError
    print(calc.calculate("3 ** 5"))  # UnknownOperationError
    print(calc.calculate(1 + 3))  # InvalidArgumentError
except (InvalidArgumentError, UnknownOperationError, InvalidOperandError, ZeroDivisionError) as e:
    print(e)
