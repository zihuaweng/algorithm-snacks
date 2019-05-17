# https://leetcode.com/problems/combination-sum/
# 同样是递归完成
# 因为出现的词语可以是重复的，所以递归self.helper中，下一步的start 可以就是上一步i
# self.helper(candidates, res, i, target - candidates[i], temp)
# ***注意res.append(temp[:]) 需要深度复制，不能使用res.append(temp)！！！

class Solution1:
    def combinationSum(self, candidates, target):
        res = []
        if not candidates:
            return res
        self.helper(candidates, res, 0, target, [])
        return res

    def helper(self, candidates, res, start, target, temp):
        if target < 0:
            return
        if target == 0:
            res.append(temp[:])
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            self.helper(candidates, res, i, target - candidates[i], temp)
            temp.pop()

# 第二种就是添加了一个排序，这样如果后面的值比target大的话就可以直接略过去，减少不必要的计算
# Runtime: 56 ms, faster than 99.39% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.1 MB, less than 64.95% of Python3 online submissions for Combination Sum.
class Solution2:
    def combinationSum(self, candidates, target):
        res = []
        if not candidates:
            return res

        candidates.sort()

        self.helper(candidates, res, 0, target, [])
        return res

    def helper(self, candidates, res, start, target, temp):
        if target == 0:
            res.append(temp[:])
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            temp.append(candidates[i])
            self.helper(candidates, res, i, target - candidates[i], temp)
            temp.pop()

a = Solution1()
print(a.combinationSum([2, 3, 5], 8))
