"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


MAPPINGS = {chr(i + ord('a') - 1): f'{i}' for i in range(1, 27)}
REVERSE_MAPPINGS = {v: k for k, v in MAPPINGS.items()}


def decode(data):
    w, ways = 0, [1, 0]
    for i in range(len(data)):
        w = 0
        w += ways[0]
        if i > 0 and data[i - 1: i + 1] in REVERSE_MAPPINGS:
            w += ways[1]
        ways[1] = ways[0]
        ways[0] = w
    return ways[0]


def main():
    data = '111'
    assert decode(data) == 3

    data = '711721'
    assert decode(data) == 6


if __name__ == '__main__':
    main()
