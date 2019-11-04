#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 首先存进去map
# 然后使用二分搜索找到小于的值
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timemap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))
        return ""

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        lst = self.timemap[key]
        if timestamp < lst[0][0]:
            return ""
        if timestamp >= lst[-1][0]:
            return lst[-1][1]
        s = 0
        e = len(lst) - 1
        while s <= e:
            mid = (s + e) >> 1
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            if lst[mid][0] < timestamp:
                if lst[mid + 1][0] > timestamp:
                    return lst[mid][1]
                s = mid + 1
            else:
                e = mid - 1
        if lst[s][0] <= timestamp:
            return lst[s][0]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
