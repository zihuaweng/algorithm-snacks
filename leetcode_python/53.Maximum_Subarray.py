# https://leetcode.com/problems/maximum-subarray/
# 使用动态规划的思想， O(n)解决问题
# temp_sum保存前面所有的和
# total_sum保存最大的和
# 如果temp_sum<0，那后面加上一个数会比单独这数要小，所以抛弃前面的和，temp_sum=这个数
# 可以用Max来写，也可以写一个if判断


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        cur = 0
        for n in nums:
            if cur < 0:
                cur = n
            else:
                cur += n
            total = max(cur, total)

        return total


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            temp = dp[i - 1] if dp[i - 1] > 0 else 0
            dp[i] = nums[i] + temp
            max_sum = max(max_sum, dp[i])

        return max_sum