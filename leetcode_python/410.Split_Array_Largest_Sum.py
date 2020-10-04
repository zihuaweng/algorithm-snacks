#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        - get the avg of arr for each subarry
            sum(arr) // m
            the result should be very close to the avg, bigger than avg
        
        we need to search between avg to sum(arr), find one value that could split arr into m
        - binary search left: avg, right: sum(arr)
        
        - range avg (3) to 15
        - 9
        split arr with sum(subarray) <= 9
        [1,2,3,4,5]
        
        1,2,3 | 4,5 => count = 2 == m, which means if we want even smaller, we need to decrease target, move left, mid
        result = 9  
        
        - range 3, 9
        - target 6
        [1,2,3,4,5]
        
        1,2,3 | 4 | 5 => count = 3 > m, increase target, move right, mid+1
        
        - range 6, 9
        - target 7
        [1,2,3,4,5]
        
        1,2,3 | 4 | 5 => count = 3 > m, increase target, move right, mid+1
        
        valid: count <= m : move left
        invalid: count > m or could not split: move right
        
        time O(logk)   k is the (sum) of nums
        space O(1)
        
        """
        hi = sum(nums)
        low = sum(nums) // m
        
        while low < hi:
            mid = (low+hi) // 2
            if self.is_valid(nums, mid, m):
                hi = mid    # 因为mid本身也是valid的，所以要包含进来
            else:
                low = mid + 1
                
        return low
            
            
    def is_valid(self, nums, target, m):
        count = 0
        cur_sum = 0
        for i, val in enumerate(nums):
            # if val > target, it can't be split
            if val > target:
                return False
            
            if cur_sum + val <= target:
                cur_sum += val
            else:
                count += 1
                cur_sum = val
        count += 1
        return count <= m
        

# https://leetcode.com/problems/split-array-largest-sum/discuss/141497/AC-Java-DFS-%2B-memorization
# dp 做法
# https://leetcode.com/problems/split-array-largest-sum/discuss/89821/Python-solution-dp-and-binary-search