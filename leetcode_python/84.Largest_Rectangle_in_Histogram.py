#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        if not heights:
            return area
        stack = [-1]  # coner case. 解决stack最后一个的左边界问题
        heights.append(0)  # coner case。解决height最后一个右边界问题
        for idx, h in enumerate(heights):
            # 发现有比最后一个小的，计算面积
            while h < heights[stack[-1]]:
                cur_idx = stack.pop()
                right_idx = idx
                # 如果有相同的可以不用处理
                while heights[stack[-1]] == heights[cur_idx]:
                    stack.pop()
                left_idx = stack[-1]
                area = max(area, heights[cur_idx] * (right_idx - left_idx - 1))

            # 其余递增的则直接加入到stack里面
            stack.append(idx)

        return area
