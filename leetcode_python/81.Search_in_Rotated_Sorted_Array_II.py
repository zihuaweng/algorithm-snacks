#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid

            elif nums[mid] < nums[start]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[start] == target:
                    return True
                start += 1

        if nums[start] == target or nums[end] == target:
            return True
        return False
