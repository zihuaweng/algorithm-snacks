# https://leetcode.com/problems/next-permutation/
# 从后面往前面找， 后面序列需要是递减的，所以找到第一个前面比后面小的值a。
# 接着从a往后找，找到第一个比a小的值b，替换
# 最后翻转b（原来a的位置）后面的值


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 2
        while n >= 0 and nums[n + 1] <= nums[n]:
            n -= 1

        if n >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[n]:
                j -= 1
            nums[n], nums[j] = nums[j], nums[n]

        start = n + 1
        end = len(nums) - 1
        while end > start:
            nums[end], nums[start] = nums[start], nums[end]
            end -= 1
            start += 1







