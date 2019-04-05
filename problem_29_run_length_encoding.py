"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


import re


def encode(data):
    return ''.join(f'{len(v.group(0))}{v.group(1)}' for v in re.finditer(r'(\w)\1*', data))


def decode(data):
    return ''.join(f'{v.group(2)*int(v.group(1))}' for v in re.finditer(r'(\d+)(\w)', data))


def main():

    x = 'AAAABBBCCDAA'
    y = '4A3B2C1D2A'

    assert encode(x) == y
    assert decode(y) == x


if __name__ == '__main__':
    main()
