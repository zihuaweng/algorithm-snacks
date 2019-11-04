#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/guess-the-word/
# https://leetcode.com/problems/guess-the-word/discuss/160945/Python-O(n)-with-maximum-overlap-heuristic
# 还没有更改答案

# Time complexity: O()
# Space complexity: O()


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n = 0
        while n < 6:
            word = random.choice(wordlist)
            n = master.guess(word)
            wordlist = [w for w in wordlist if sum(g == w for g, w in zip(word, w)) == n]