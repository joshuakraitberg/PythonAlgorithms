"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
Bonus: Can you do this with three numbers?
"""


def contains_sum(x, k):
    cache = set()
    for v in x:
        d = k - v
        if d in cache:
            return v, d
        else:
            cache.add(v)
    return None


def contains_three_sum(x, k):
    """O( ((n - 2)^2 +(n + 2))/2 + (n - 2) )"""
    cache = {}
    for i, iv in enumerate(x[:-2]):
        for j, jv in enumerate(x[i + 1:], i + 1):
            d = k - jv
            tag = tuple(sorted((i, j)))
            if d in cache and all(j not in c for c in cache[d]):
                c = next(iter(cache[d]))
                return x[c[0]], x[c[1]], jv
            else:
                t = iv + jv
                cache.setdefault(t, set()).add(tag)
    return None


def main():
    k = 17
    x = [10, 15, 3, 7]
    assert bool(contains_sum(x, k))

    k = 114
    x = [10, 15, 3, 7, -1, 100, 12, 12]
    assert bool(contains_three_sum(x, k))


if __name__ == '__main__':
    main()
