"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""


def find_longest_palindrome(string):

    pos = 1
    length = 1
    longest = ''
    half = len(string) // 2

    def find_odd_palindrome(x):
        for i, (u, v) in enumerate(zip(string[x + 1:], string[:x][::-1])):
            if v != u or v.isspace():
                return i
        return min(x, half)

    while True:
        for i, c in enumerate(string[pos:-pos], pos):
            if c.isspace():
                continue
            n = find_odd_palindrome(i)
            if n > length:
                length = n
                longest = string[i-n+1:i+n]
                break
        else:
            return longest


def main():
    assert find_longest_palindrome('aabcdcb') == 'bcdcb'
    assert find_longest_palindrome('banana') == 'anana'


if __name__ == '__main__':
    main()
