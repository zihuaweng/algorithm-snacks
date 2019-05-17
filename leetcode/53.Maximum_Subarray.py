# https://leetcode.com/problems/maximum-subarray/
# 使用动态规划的思想， O(n)解决问题
# temp_sum保存前面所有的和
# total_sum保存最大的和
# 如果temp_sum<0，那后面加上一个数会比单独这数要小，所以抛弃前面的和，temp_sum=这个数
# 可以用Max来写，也可以写一个if判断


class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        temp_sum = nums[0]
        total_sum = nums[0]
        for i in nums[1:]:
            temp_sum = max(temp_sum + i, i)
            total_sum = max(temp_sum, total_sum)

        return total_sum
