# https://leetcode.com/problems/course-schedule/
# https://blog.csdn.net/fuxuemingzhu/article/details/82951771
# 拓扑排序 ， dfs
# 这个题目目标是寻找一个有向无环图，如果有，则不能完成所有课程，如果没有则可以完成所有课程
#


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)

        # 0：没有走过
        # 1：正在走
        # 2：已经走过了
        visited = [0] * numCourses

        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
        return True

    def dfs(self, key, visited, graph):
        if visited[key] == 1:
            return False
        if visited[key] == 2:
            return True
        visited[key] = 1
        for edge in graph[key]:
            if not self.dfs(edge, visited, graph):
                return False
        visited[key] = 2
        return True
