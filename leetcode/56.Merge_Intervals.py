# https://leetcode.com/problems/merge-intervals/
# 首先排序，遇到下一个的开始在上一个中间，替换一个终止

class Solution:
    def merge(self, intervals: list) -> list:
        if not intervals:
            return []
        res = []
        intervals = sorted(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= end:
                if end < i[1]:
                    end = i[1]
            else:
                res.append([start, end])
                start = i[0]
                end = i[1]

        res.append([start, end])

        return res