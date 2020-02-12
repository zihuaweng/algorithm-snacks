#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sliding-puzzle/

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(a) for b in board for a in b)
        queue = collections.deque()
        queue.append((s, s.index('0')))
        seen = set((s, s.index('0')))

        # directions
        step = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                t, idx = queue.popleft()
                if t == '123450':
                    return step
                i = idx // 3
                j = idx % 3
                for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= x < 2 and 0 <= y < 3:
                        idx_n = 3 * x + y
                        a = list(t)
                        a[idx], a[idx_n] = a[idx_n], a[idx]
                        t_n = ''.join(a)
                        if (t_n, idx_n) not in seen:
                            seen.add((t_n, idx_n))
                            queue.append((t_n, idx_n))

            step += 1
        return -1

