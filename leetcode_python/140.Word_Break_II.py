#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/word-break-ii/
# dfs 解决，每次看开头是否符合，符合递归后面的s[len(word):]

# Time complexity: O(n*k*n)
# Space complexity: O()


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(s, memo):
            if s in memo:
                return memo[s]
            if not s:
                return []
            res = []
            for word in wordDict:
                if s.startswith(word):
                    if len(s) == len(word):
                        res.append(word)
                    else:
                        next_res = dfs(s[len(word):], memo)
                        for i in next_res:
                            res.append(word + ' ' + i)

            memo[s] = res
            return res

        return dfs(s, {})
