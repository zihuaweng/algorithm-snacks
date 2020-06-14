#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/string-transforms-into-another-string/


# Time complexity: O(n)
# Space complexity: O()

# 因为每次转换，所有str1中所有相同的char都要转换
# 例如 ： ab -> ba
# 第一步： a转换成b，就有bb，第二个转换b -> 整个字符串会变成aa
# 所以，转换中出现有环，a->b->a
# 我们需要首先b->temp, a->b, temp->a
# 所以我们需要额外的一个char来做中间转换，如果所有26字母都用上了，就没有temp来完成转换
# 选择判断len(set(str2)) < 26是因为所有str1对str2可以多对一，所以len(set(str2)) <= len(set(str1))
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        l = len(str1)
        d = {}
        for a, b in zip(str1, str2):
            if d.setdefault(a, b) != b:
                return False
        return len(set(str2)) < 26

