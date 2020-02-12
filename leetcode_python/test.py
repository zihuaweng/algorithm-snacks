#!/usr/bin/env python3
# coding: utf-8

def a(f):
    m = len(f)
    n = len(f[0])
    seen = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if seen[i][j] == 0 and helper(seen, f, i, j, m, n, -1, -1):
                return True
    return False


def helper(seen, f, i, j, m, n, pre_r, pre_c):
    seen[i][j] = 1
    for _x, _y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = i + _x
        new_y = j + _y
        if new_x == pre_r and new_y == pre_c:
            continue
        if 0 <= new_x < m and 0 <= new_y < n and f[new_x][new_y] == '1':
            if seen[new_x][new_y] == 1 or helper(seen, f, new_x, new_y, m, n, i, j):
                return True
    # seen[i][j] = 2
    return False


def helper2(seen, f, i, j, m, n, pre_r, pre_c):
    seen[i][j] = 1
    for _x, _y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = i + _x
        new_y = j + _y
        if new_x == pre_r and new_y == pre_c:
            continue
        if 0 <= new_x < m and 0 <= new_y < n and f[new_x][new_y] == '1':
            if seen[new_x][new_y] == 1 or (seen[new_x][new_y] == 0 and helper2(seen, f, new_x, new_y, m, n, i, j)):
                return True
    seen[i][j] = 2
    return False


foo = [['B', 'B', 'B', 'B', 'B'],
       ['B', 'G', 'G', 'G', 'B'],
       ['B', 'G', 'B', 'G', 'B'],
       ['B', 'G', 'G', 'G', 'B'],
       ['B', 'B', 'B', 'B', 'D']]
foo2 = [[0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]]

print(a(foo2))
