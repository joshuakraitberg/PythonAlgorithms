"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""


def calculate_fillable_units(x):
    high, low, carry, total, span = x[0], 0, 0, 0, 0
    for v in x[1:]:
        span += 1
        if v >= high:
            total += carry
            high, low, carry, span = v, 0, 0, 0
        elif v < high:
            carry += high - v
            low = max(v, low)
    if span > 0 and low > 0:
        total += carry - (high - low)*span - low
    return total


def main():

    x = [3, 0, 1, 3, 0, 5]
    y = 8

    assert calculate_fillable_units(x) == y

    x = [0, 1, 3, 0, 1, 3, 0, 5, 0, 2, 2, 2, 3, 0]
    y = 14

    assert calculate_fillable_units(x) == y


if __name__ == '__main__':
    main()
