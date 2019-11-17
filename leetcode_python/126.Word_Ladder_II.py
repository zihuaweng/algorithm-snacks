#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        words = set(wordList)
        if endWord not in words:
            return res

        graph = collections.defaultdict(set)
        q = set()
        q.add(beginWord)
        next_q = set()
        found = False
        while q and not found:
            words -= q
            for w in q:
                # 替换每个w里面每个字母
                for i in range(len(w)):
                    for e in 'qwertyuiopasdfghjklzxcvbnm':
                        new_w = w[:i] + e + w[i + 1:]
                        if new_w in words:
                            graph[w].add(new_w)
                            if new_w == endWord:
                                found = True
                            else:
                                next_q.add(new_w)

            q = next_q
            next_q = set()

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in graph[x] for rest in bt(y)]

        return bt(beginWord)

# 另一种实现
class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        words = set(wordList)
        if endWord not in words:
            return res

        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            new_layer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(lst for lst in layer[w])
                else:
                    for i in range(len(w)):
                        for e in 'qwertyuiopasdfghjklzxcvbnm':
                            new_w = w[:i] + e + w[i + 1:]
                            if new_w in words:
                                new_layer[new_w] += [lst + [new_w] for lst in layer[w]]
            words -= new_layer.keys()
            layer = new_layer
            # print(layer)

        return res