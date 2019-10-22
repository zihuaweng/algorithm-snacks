# https://leetcode.com/problems/product-of-array-except-self/
# 左边向右边遍历每次多乘前面一个值
# 同时从后向前，每个值要多乘后面的值
# Time complexity: O(n)
# Space complexity: O(n)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        right = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
            res[len(nums) - 1 - i] *= right
            right *= nums[len(nums) - 1 - i]

        return res
