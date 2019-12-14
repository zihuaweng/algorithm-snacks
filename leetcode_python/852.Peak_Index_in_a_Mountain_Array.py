#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        j = len(A)-1
        while i<= j:
            mid = (i+j)//2
            if A[mid] < A[mid+1]:
                i = mid + 1
            else:
                j = mid - 1
        return i


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        j = len(A)-1
        while i< j:
            mid = (i+j)//2
            if A[mid] < A[mid+1]:
                i = mid + 1
            else:
                j = mid
        return i