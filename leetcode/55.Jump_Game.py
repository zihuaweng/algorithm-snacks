# https://leetcode.com/problems/jump-game/
# 往前移动，记录可以到达的最远的位置max_step，每次移动的范围要小于max_step
# 如果max_step大于等于最后的index，返回true


class Solution:
    def canJump(self, nums:list) -> bool:
        max_step = 0
        i = 0
        while i < len(nums) and i <= max_step:
            max_step = max(max_step, i + nums[i])
            if max_step >= len(nums) - 1:
                return True
            i += 1
        return False
