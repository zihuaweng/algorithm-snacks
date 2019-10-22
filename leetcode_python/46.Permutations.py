# https://leetcode.com/problems/permutations/
# ****注意：res.append(temp[:]) 不可以使用 res.append(temp)， 因为这样会后面temp更改，res里面的内容也会被更改！！


class Solution:
    def permute(self, nums):
        if not nums:
            return []

        length = len(nums)
        res = []
        used = [0] * length
        temp_list = []
        self.helper(nums, used, temp_list, res)
        return res

    def helper(self, nums, used, temp, res):

        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(used)):
            if used[i] == 0:
                temp.append(nums[i])
                used[i] = 1
                self.helper(nums, used, temp, res)
                temp.pop()
                used[i] = 0


a = Solution()
out = a.permute([1,2,3])
print('------')
print(out)