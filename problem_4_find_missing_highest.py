"""
Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def find_missing_int(x):

    # Move invalids to end
    end = len(x) - 1
    for i in range(len(x))[::-1]:
        if x[i] <= 0 or x[i] > len(x):
            x[end], x[i] = x[i], x[end]
            end -= 1
    end += 1

    # Sort valid numbers
    for i in range(end)[::-1]:
        x[x[i] - 1], x[i] = x[i], x[x[i] - 1]
    for i in range(end):
        x[x[i] - 1], x[i] = x[i], x[x[i] - 1]

    # Find missing highest valid
    for i in range(end):
        if x[i] != i + 1:
            return i + 1

    return end + 1


def main():

    x = [3, 4, -1, 1]
    assert find_missing_int(x) == 2

    x = [1, 2, 0]
    assert find_missing_int(x) == 3

    x = [7, 1, 1, 0, 9, 2, -1, 2, 3, 4, 113, -1, 5, 8, 6]
    assert find_missing_int(x) == 10


if __name__ == '__main__':
    main()
