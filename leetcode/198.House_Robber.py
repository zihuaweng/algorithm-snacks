# https://leetcode.com/problems/house-robber/
# 这道题和走楼梯一样，也是斐波那契数列改变题目
# 每个值取决于他前面第二个，和前面第三个值的大小，反正不能是前面第一个，会报警，且不能是前第四个，因为中间肯定还有一个值可以加

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        res_list = [0] * 3
        res_list[0] = nums[0]
        res_list[1] = max(nums[0], nums[1])
        res_list[2] = max(nums[0] + nums[2], nums[1])

        for i in range(3, len(nums)):
            index = i % 3
            last_1 = (i - 2) % 3
            last_2 = (i - 3) % 3
            res_list[index] = nums[i] + max(res_list[last_1], res_list[last_2])

        return max(res_list)
