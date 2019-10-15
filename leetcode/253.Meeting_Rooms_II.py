#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/meeting-rooms-ii/

# Time complexity: O(nlogn) (因为排序了)
# Space complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = s = 0 # 记录当前开始和终止指针位置
        numRooms = available = 0
        while s < len(starts):
            # 如果每个间断开始都比第一个结束的要早，这些都需要用新的房间
            # 如果available（之前腾空的房间），就从里面扣除
            if starts[s] < ends[e]:
                s += 1
                if available:
                    available -= 1
                else:
                    numRooms += 1
            else:
                # 证明有一个房间用完了，加进去available
                # 更新终止时间
                # 注意：但是这个start其实还没有开始房间去房间，所以start还是当前指针！！！！
                available += 1
                e += 1

        return numRooms