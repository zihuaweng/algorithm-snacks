#!/usr/bin/env python3
# coding: utf-8

# hard 题目
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 比较好的解释https://www.youtube.com/watch?v=LPFhl65R7ww&feature=youtu.be&t=1441
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
# https://windliang.cc/2018/07/18/leetCode-4-Median-of-Two-Sorted-Arrays/

# Time complexity: O(log(min(m, n)))
# Space complexity: O()


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 首先保证len(nums1) < len(nums2)
        x = len(nums1)
        y = len(nums2)
        if x > y:
            nums1, nums2 = nums2, nums1
            x, y = y, x

        start = 0
        end = x
        while start <= end:
            # nums1的分割点
            p1 = (end + start) // 2
            # nums2的分割点
            # 加一的原因是分割出来的两部分，x,y的左边所有数目在奇数情况个数更多，
            # 所以后面奇数的情况可以使用return max(max_left_x, max_left_y)
            p2 = (x + y + 1) // 2 - p1
            # 会出现边际问题，需要定义最大最小做比较
            max_left_x = float('-inf') if p1 == 0 else nums1[p1 - 1]
            min_right_x = float('inf') if p1 == x else nums1[p1]
            max_left_y = float('-inf') if p2 == 0 else nums2[p2 - 1]
            min_right_y = float('inf') if p2 == y else nums2[p2]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                end = p1 - 1
            else:
                start = p1 + 1
