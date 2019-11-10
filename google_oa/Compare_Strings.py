#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/discuss/interview-question/352458/


# def solve(A, B):
#     A = A.split(',')
#     B = B.split(',')
#     ans = []
#     for b in B:
#         counter = 0
#         for a in A:
#             if b.count(min(b)) > a.count(min(a)):
#                 counter += 1
#         ans.append(counter)
#     return ans

class Solution:
    def compare(self, A, B):
        A = A.split(',')
        B = B.split(',')
        freq_count = [0] * 11
        res = []

        for a in A:
            freq = a.count(min(a))
            freq_count[freq] += 1

        for b in B:
            count = b.count(min(b))
            res.append(sum(freq_count[:count]))

        return res


a = Solution()
print(a.compare('abcd,aabc,bd', 'aaa,aa'))
print(a.compare('abcd,aaabc,bbd', 'aaa,aa'))
