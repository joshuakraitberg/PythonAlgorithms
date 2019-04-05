"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def create_balance_tester(balance):
    balance_check = {v: k for k, v in balance.items()}

    def tester(expr):
        stack = []
        for c in expr:
            if c in balance:
                stack.append(c)
            elif c in balance_check and balance_check[c] != stack.pop():
                return False
        return len(stack) == 0
    return tester


regular_balance_tester = create_balance_tester({'(': ')', '[': ']', '{': '}'})


def main():

    expr = '([])[]({})'
    assert regular_balance_tester(expr)

    expr = '([)}'
    assert not regular_balance_tester(expr)

    expr = '((()'
    assert not regular_balance_tester(expr)


if __name__ == '__main__':
    main()
