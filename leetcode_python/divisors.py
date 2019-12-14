#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 计算约数个数

# 时间复杂度 O(n)
def fun1(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count


# 时间复杂度 O( sqrt(n) )
def fun2(num):
    count = 0
    sqrt = int(num**0.5)
    for x in range(1, sqrt+1):
        if num % x == 0:
            count += 2
    return count - (sqrt **2 ==num)

print(fun2(12))
print(fun2(4))
print(fun2(10))
