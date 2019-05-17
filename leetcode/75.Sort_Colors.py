class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        for i in range(2):
            for j in range(head, len(nums)):
                if nums[j] == i:
                    nums[head], nums[j] = nums[j], nums[head]
                    head += 1

