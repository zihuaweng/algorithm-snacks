#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/reorder-data-in-log-files/


# Time complexity: O()
# Space complexity: O()


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            first, rest = log.split(" ", 1)
            return (0, rest, first) if rest[0].isalpha() else (1,)
        return sorted(logs, key = f)