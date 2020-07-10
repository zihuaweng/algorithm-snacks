## https://leetcode.com/problems/3sum/
## 这道题重点在于2sum怎么计算。
## 首先排序，设置两个指针，向中间移动
## 3sum/4sum就是前面加一个循环，遍历前面一个+2sum 或者遍历前面两个+2sum


class Solution:
    def threeSum(self, nums):
        res = []
        if not nums or len(nums) < 3:
            return res
        nums = sorted(nums)
        length = len(nums)
        for i in range(length - 2):
            # pruning : because the list is sort, if one > 0 then we can return res.
            if nums[i] > 0:
                return res
            # pruning : 记得需要排除第一个位置重复项，如果是0前面没有就不用判断
            if i != 0 or nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = length - 1
            target = -nums[i]
            while start < end:
                if nums[start] + nums[end] == target:
                    res.append([nums[i], nums[start], nums[end]])
                    ## 这里同样需要排除重复的项
                    while start < end and nums[start + 1] == nums[start]:
                        start += 1
                    while start < end and nums[end - 1] == nums[end]:
                        end -= 1
                    start += 1
                    end -= 1

                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    start += 1

        return res
