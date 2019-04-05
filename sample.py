"""
There's a staircase with N steps,
and you can climb 1 or 2 steps at a time.
Given N, write a function that returns the number
of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
Generalize your function to take in X.
"""


def staircase(steps, step_sizes):
    """Climb `steps` using a combination of `step_sizes`.

    @:param steps: Number of steps in staircase.
    @:param step_sizes: Set of possibles step sizes that can be taken as single action.
    @:return: List of all possible combinations of step actions to complete staircase
    """

    cache = [0 for _ in range(steps + 1)]
    cache[0] = 1
    for i in range(1, steps + 1):
        cache[i] += sum(cache[i - x] for x in step_sizes if i - x >= 0)
    return cache[steps]


def main():
    n = 4
    s = [1, 2]
    r = staircase(n, s)
    print(f'N={n} + S={s} -> R={r}')


if __name__ == '__main__':
    main()
