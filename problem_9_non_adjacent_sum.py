"""
Given a list of integers,
write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13,
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_sum_non_adjacent(x):
    inc = 0  # Max sum including current element
    exc = 0  # Max sum excluding current element
    for v in x:
        # Current max excluding current element
        # Determine if taking previous element
        new_exc = exc if exc > inc else inc
        # Current max including current element
        inc = exc + v
        exc = new_exc
    return exc if exc > inc else inc


def main():
    x = [2, 4, 6, 7, 2, 5, 7]
    assert largest_sum_non_adjacent(x) == 18

    x = [2, 4, 6, 2, 5]
    assert largest_sum_non_adjacent(x) == 13

    x = [5, 1, 1, 5]
    assert largest_sum_non_adjacent(x) == 10


if __name__ == '__main__':
    main()
