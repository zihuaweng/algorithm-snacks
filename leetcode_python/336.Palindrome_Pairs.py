#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/palindrome-pairs/
# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {w: i for i, w in enumerate(words)}
        print(d)
        res = set()
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                pre, pos = w[:j], w[j:]
                if pre == pre[::-1] and pos[::-1] in d and d[pos[::-1]] != i:
                    res.add((d[pos[::-1]], i))
                if pos == pos[::-1] and pre[::-1] in d and d[pre[::-1]] != i:
                    res.add((i, d[pre[::-1]]))

        return res