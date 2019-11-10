#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/discuss/interview-question/396769/

class Solution:
    def get_time(self, time):
        ans = list('23:59')
        time = list(time)

        if time[0] == '?':
            if time[1] != '?' and time[1] > '3':
                ans[0] = '1'

        if time[1] == '?':
            if time[0] != '?' and time[0] < '2':
                ans[1] = '9'

        for i in range(len(time)):
            if time[i] != '?':
                ans[i] = time[i]

        return ''.join(ans)


a = Solution()
print(a.get_time('??:59'))
print(a.get_time('?4:?8'))
print(a.get_time('?3:?9'))
print(a.get_time('0?:??'))
print(a.get_time('1?:??'))
print(a.get_time('??:??'))
print(a.get_time('?5:?9'))
print(a.get_time('?9:??'))