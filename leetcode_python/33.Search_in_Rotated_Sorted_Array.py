# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 使用二分法找到位置。
# 首先确定每次中间的值的位置，与前面是顺序的还是与后面是顺序的
# 然后判断中间值是否在顺序的内容里，确定下一步的界限，接下来重复这两个判断，剩下两个值，如果两个值都没有则返回-1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(l,r, mid)

            if target == nums[mid]:
                return mid

            if nums[mid] < nums[r]:   # eg. 5,6,1,2,3,4
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:   # eg. 3,4,5,6,1,2
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif nums[l] < target < nums[mid]:
                r = mid-1
            elif nums[mid] < target < nums[r]:
                l = mid+1
            else:
                l += 1
                r -= 1
        return -1
