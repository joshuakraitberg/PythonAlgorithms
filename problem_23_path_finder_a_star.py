"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down, and right.
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left),
the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

import sys
import heapq
import logging


log = logging.getLogger(__name__)
hlr = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter('%(levelname)5s: %(message)s')
hlr.setFormatter(fmt)
log.addHandler(hlr)
log.setLevel(logging.DEBUG)


class TileStep(object):
    def __init__(self, n, pos, prev, k):
        self.n = n
        self.pos = pos
        self.prev = prev
        self.k = k + n

    def __lt__(self, other):
        return self.k < other.k

    def __gt__(self, other):
        return self.k > other.k

    def __eq__(self, other):
        return self.k == self.k


def dst(a, b):
    return pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 0.5)


def find_next_steps(pos, board):
    return (v for v in (
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] - 1),
    ) if 0 <= v[0] < len(board[0]) and 0 <= v[1] <= len(board) and board[v[0]][v[1]] is False)


def find_path(start, end, board):
    log.debug(f'start -> {start}')
    log.debug(f'end -> {end}')

    heap = []
    board[start[0]][start[1]] = True
    heapq.heappush(heap, TileStep(0, start, None, dst(start, end)))
    while heap:
        tile = heapq.heappop(heap)
        log.debug(f'tile(n, pos, k) -> ({tile.n}, {tile.pos}, {tile.k})')
        if tile.pos == end:
            steps = [tile.pos]
            tile = tile.prev

            while tile:
                steps.append(tile.pos)
                tile = tile.prev
            return steps[-2::-1]
        for s in find_next_steps(tile.pos, board):
            log.debug(f'neighbour -> {s}')
            board[s[0]][s[1]] = True
            heapq.heappush(heap, TileStep(tile.n + 1, s, tile, dst(s, end)))
    return []


def main():
    start = (3, 0)
    end = (0, 0)
    board = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]
    ]
    steps = find_path(start, end, board)
    log.info(steps)
    assert len(steps) == 7


if __name__ == '__main__':
    main()
