#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(NlogK)
# Space complexity: O()

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        heap = [(math.sqrt(x ** 2 + y ** 2), idx) for idx, (x, y) in enumerate(points)]
        heapq.heapify(heap)
        res = []
        for i in range(K):
            cur = heapq.heappop(heap)
            res.append(points[cur[1]])

        return res


# 另一种写法
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        heap = []
        heapq.heapify(heap)
        for idx, (x, y) in enumerate(points):
            if idx < K:
                heapq.heappush(heap, (-math.sqrt(x ** 2 + y ** 2), idx))
            else:
                if heap[0][0] < -math.sqrt(x ** 2 + y ** 2):
                    heapq.heappushpop(heap, (-math.sqrt(x ** 2 + y ** 2), idx))

        res = [points[i[1]] for i in heap]

        return res