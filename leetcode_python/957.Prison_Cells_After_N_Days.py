#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {str(cells): N}

        while N:
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            N -= 1
            if str(cells) in seen:
                N %= seen[str(cells)] - N
            else:
                seen[str(cells)] = N

        return cells