#!/usr/bin/env python3
# coding: utf-8


# https://leetcode.com/discuss/interview-question/352459/

# Time complexity: O()
# Space complexity: O()


class Solution:
    def largest_subarray(self, a, k):
        idx = 0
        for i in range(1, len(a) - k + 1):
            if a[idx] < a[i]:
                idx = i

        return a[idx:idx + k]


# nonunique
class Solution:
    def largest_subarray(self, a, k):
        idx = 0
        for i in range(1, len(a)-k+1):
            for j in range(k):
                if a[idx+j] < a[i+j]:
                    idx = i
                    break
                elif a[idx+j] > a[i+j]:
                    break
                else:
                    continue
        return a[idx:idx+k]

a = Solution()
print(a.largest_subarray([1, 4, 3, 2, 5], 4))
print(a.largest_subarray([9, 4, 3, 2, 5], 4))
print(a.largest_subarray([0, 0, 1, 3, 2, 5], 4))