#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/backspace-string-compare/

# Time complexity: O()
# Space complexity: O(1)


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_idx = len(S) - 1
        t_idx = len(T) - 1

        s_count = 0
        t_count = 0

        while s_idx >= 0 or t_idx >= 0:
            while s_idx >= 0 and (s_count > 0 or S[s_idx] == '#'):
                if S[s_idx] == '#':
                    s_count += 1
                else:
                    s_count -= 1
                s_idx -= 1
            left = S[s_idx] if s_idx >= 0 else '$'

            while t_idx >= 0 and (t_count > 0 or T[t_idx] == '#'):
                if T[t_idx] == '#':
                    t_count += 1
                else:
                    t_count -= 1
                t_idx -= 1

            right = T[t_idx] if t_idx >= 0 else '$'
            if right != left:
                return False

            s_idx -= 1
            t_idx -= 1

        return True