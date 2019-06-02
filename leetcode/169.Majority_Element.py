# https://leetcode.com/problems/majority-element/
# Boyer-Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        max_num = nums[0]
        for num in nums[1:]:
            if count == 0:
                count = 1
                max_num = num
            else:
                if num == max_num:
                    count += 1
                else:
                    count -= 1
        return max_num
