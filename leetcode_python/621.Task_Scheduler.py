#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/task-scheduler/
# https://www.youtube.com/watch?v=OQKpjr13VNk

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        tasks_counter = collections.Counter(tasks)
        tasks_c = list(tasks_counter.values())
        tasks_c.sort(reverse=True)
        max_length = tasks_c[0] - 1
        space = max_length * n
        for i in tasks_c[1:]:
            space -= min(max_length, i)

        return max(len(tasks) + space, len(tasks))
