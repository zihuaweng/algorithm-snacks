# https://leetcode.com/discuss/interview-question/854110/

import heapq

def five_star_seller(nums, threshold): # productRatings =[[4,4],[1,2],[3,6]], percentage rating threshold = 77
    heap = []
    res = 0
    
    for i, val in enumerate(nums):
        dd, d = val
        diff = get_diff(dd, d)
        heapq.heappush(heap, (-diff, i))

    while get_sum(nums) < threshold / 100:
        _, idx = heapq.heappop(heap)
        nums[idx][0] += 1
        nums[idx][1] += 1

        diff = get_diff(nums[idx][0], nums[idx][1])
        heapq.heappush(heap, (-diff, idx))
        res += 1
        print(nums)

    return res


def get_diff(dd, d):
    new = (dd+1) / (d+1)
    return new - dd/d


def get_sum(nums):
    n = len(nums)
    total = 0
    for dd, d in nums:
        total += dd / d
    
    return total / n


print(five_star_seller([[4,4],[1,2],[3,6]], 77))