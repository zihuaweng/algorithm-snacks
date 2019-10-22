# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 二分法

class Solution:
    def searchRange(self, nums, target: int):

        if not nums:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            if nums[mid] < target:
                start = mid
            if nums[mid] == target:
                i = mid
                j = mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1

                return [i + 1, j - 1]

        if nums[start] == target and nums[end] == target:
            return [start, end]
        if nums[start] == target:
            return [start, start]
        if nums[end] == target:
            return [end, end]

        return [-1, -1]

