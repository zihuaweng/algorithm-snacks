# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 使用二分法找到位置。
# 首先确定每次中间的值的位置，与前面是顺序的还是与后面是顺序的
# 然后判断中间值是否在顺序的内容里，确定下一步的界限，接下来重复这两个判断，剩下两个值，如果两个值都没有则返回-1


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid

            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
