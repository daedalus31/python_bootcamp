def rpn(*args):
    operators = ['+', '-', '*', '/']
    stack = list()
    for item in args:
        if item not in operators:
            stack.append(item)
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if item == '+':
                stack.append(n1 + n2)
            elif item == '-':
                stack.append(n1 - n2)
            elif item == '*':
                stack.append(n1 * n2)
            elif item == '/':
                stack.append(n1 / n2)
    return stack[0]


def test_rpn_add():
    assert rpn(1, 2, '+') == 3


def test_rpn_subtract():
    assert rpn(3, 2, '-') == 1


def test_rpn_example():
    assert rpn(2, 3, '+', 5, '*')
