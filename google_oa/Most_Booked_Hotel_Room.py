#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/discuss/interview-question/421787/

class Solution:
    def compare(self, rooms):
        booked = dict()
        for room in rooms:
            status = room[0]
            num = room[1:]
            if status == '+':
                if num not in booked:
                    booked[num] = 1
                else:
                    if booked[num] & 1 == 0:
                        booked[num] += 1
            else:
                if num in booked and booked[num] & 1:
                    booked[num] += 1

        res = '9Z'
        count = 0
        for key, val in booked.items():
            temp = (val >> 1) + (val & 1)
            if temp >= count:
                count = temp
                res = min(res, key)

        return res


a = Solution()
print(a.compare(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))
print(a.compare(["-1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))
print(a.compare(["+1A", "+3E", "-1A", "+4F", "-1A", "-3E"]))
print(a.compare(["-1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))
print(a.compare(
    ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+1A", "+1A", "+1A", "+1A", "+1A", "+1A", "+1A", "+3E", "+3E", "+3E",
     "+3E", "+3E", "+3E"]))
