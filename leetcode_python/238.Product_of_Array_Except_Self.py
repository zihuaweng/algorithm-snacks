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


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #         [1, 2, 3, 4]

        #         [1, 1, 2, 6] left =
        #         [24, 12, 4, 1] right
        #         [1*24, 1*12, 2*4, 6]
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            nums[i] = left[i] * right[i]

        return nums




