#!/usr/bin/env python3
# coding: utf-8

def find_largest(arr):
    pre_sum = 0
    total = float('-inf')
    left = 0
    res = []
    for i, n in enumerate(arr):
        if pre_sum < 0:
            left = i
            pre_sum = 0
        
        pre_sum += n
        if pre_sum > total:
            total = pre_sum
            res = arr[left:i+1]

    return res, total


print(find_largest([-2,1,-3,4,-1,2,1,-5,4]))