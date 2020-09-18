#!/usr/bin/env python3
# coding: utf-8

# hard 题目
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://www.youtube.com/watch?v=ScCg9v921ns

# Time complexity: O(log(min(m, n)))
# Space complexity: O()


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 首先保证len(nums1) < len(nums2), 因为我们需要定pivot point，从小的入手可以保证另外一个左右两边是平分的，从大的入手有可能剩下的数少于1/2
        x = len(nums1)
        y = len(nums2)
        if x > y:
            nums1, nums2 = nums2, nums1
            x, y = y, x

        start = 0
        end = x
        while (start <= end):
            p1 = (end + start) // 2  # nums1 左边元素个数
            p2 = (x + y) // 2 - p1  # nums2 左边元素个数
            max_left_x = float('-inf') if p1 == 0 else nums1[p1 - 1]
            min_right_x = float('inf') if p1 == x else nums1[p1]
            max_left_y = float('-inf') if p2 == 0 else nums2[p2 - 1]
            min_right_y = float('inf') if p2 == y else nums2[p2]

            if max_left_x > min_right_y:
                end = p1 - 1
            elif max_left_y > min_right_x:
                start = p1 + 1
            else:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return min(min_right_x, min_right_y)
