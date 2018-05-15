def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '**':
        return num1 ** num2
    else:
        return None


def test_calculate_multiply():
    assert calculate(9, 3, '*') == 27


def test_calculate_wrong_op():
    assert calculate(2, 4, '%') is None


def test_calculate_power():
    assert calculate(2, 10, '**') == 1024
