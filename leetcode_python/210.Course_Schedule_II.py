#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/course-schedule-ii/
# 第一种方法： dfs：
# 记录每个课程的先修课个数，以及每门课后面可以上的科目。stack里面有所有不需要先修课的课程，这些课可以任意顺序选修。
# 他们后面的课程，因为当前课程已经上完，所以先修课就减1，如果遇到有先修课已经都上完的课，证明这门课可以任意选修，加进去队列中。
# Time complexity: O(n)
# Space complexity: O(n)

class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class_next = collections.defaultdict(set)
        class_pre = [0 for i in range(numCourses)]
        for c, prec in prerequisites:
            class_next[prec].add(c)
            class_pre[c] += 1
        non_pre_class = [i for i in range(numCourses) if class_pre[i] == 0]
        res = []
        while non_pre_class:
            cur = non_pre_class.pop()
            res.append(cur)
            for i in class_next[cur]:
                class_pre[i] -= 1
                if class_pre[i] <= 0:
                    non_pre_class.append(i)
        if len(res) == numCourses:
            return res
        else:
            return []

# 第一种方法： bfs：
# 先使用了一个queue （python里面for循环相当于queue），如果有走过的，吧pre_class个数删除了。
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class_next = collections.defaultdict(set)
        class_pre = [0 for i in range(numCourses)]
        for c, prec in prerequisites:
            class_next[prec].add(c)
            class_pre[c] += 1
        bfs = [i for i in range(numCourses) if class_pre[i] == 0]
        for i in bfs:
            for j in class_next[i]:
                class_pre[j] -= 1
                if class_pre[j] == 0: # 这里不能小于零，否则重复添加内容了
                    bfs.append(j)
        return bfs if len(bfs) == numCourses else []