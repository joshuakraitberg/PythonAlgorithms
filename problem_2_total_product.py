"""
Given an array of integers,
return a new array such that each element at index i
of the new array is the product of all the numbers in
the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def total_product(x):
    y = [1]*len(x)
    for i, v0 in enumerate(x[:-1]):
        for j, v1 in enumerate(x[i + 1:], i + 1):
            y[i] *= v1
            y[j] *= v0
    return y


def main():
    x = [1, 2, 3, 4, 5]
    assert total_product(x) == [120, 60, 40, 30, 24]

    x = [3, 2, 1]
    assert total_product(x) == [2, 3, 6]


if __name__ == '__main__':
    main()
