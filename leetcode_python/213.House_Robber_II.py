#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        r_r = nums[0]
        nr_r = r_nr = nr_nr = 0

        for num in nums[1:]:
            pre_r = max(r_r, nr_r)
            r_r = nr_r + num
            nr_r = pre_r
            # print(r_r, nr_r)

            pre_nr = max(r_nr, nr_nr)
            r_nr = nr_nr + num
            nr_nr = pre_nr
            # print(r_nr, nr_nr)

        return max(nr_r, r_nr)
