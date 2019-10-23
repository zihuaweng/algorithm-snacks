#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/text-justification/

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        temp = []
        word_length = 0
        for w in words:
            if word_length + len(w) + len(temp) <= maxWidth:
                temp.append(w)
                word_length += len(w)
            else:
                # 分配所有的空格，round robin logic
                space = maxWidth - word_length
                length = len(temp) - 1
                for i in range(space):
                    # 有可能这一行是只有一个元素，length=0， 那么%报错，length or 1 会自动选择1
                    temp[i % (length or 1)] += " "
                res.append(''.join(temp))
                # 新的一个循环
                temp = [w]
                word_length = len(w)
        # 最后一行：
        res.append(' '.join(temp).ljust(maxWidth))

        return res




