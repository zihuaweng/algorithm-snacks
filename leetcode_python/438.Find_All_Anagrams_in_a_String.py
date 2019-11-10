#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 很好的总结
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(s)
        m = len(p)
        if m > n:
            return res

        counter = collections.Counter(p)
        length = len(counter)
        slow = fast = 0
        while fast < n:
            if s[fast] in counter:
                counter[s[fast]] -= 1
                if counter[s[fast]] == 0:
                    length -= 1
            fast += 1

            while length == 0:
                if s[slow] in counter:
                    if counter[s[slow]] == 0:
                        length += 1
                    counter[s[slow]] += 1

                if fast - slow == m:
                    res.append(slow)

                slow += 1
        return res
