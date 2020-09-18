# https://leetcode.com/problems/critical-connections-in-a-network/
# space: O(n)
# time: O(n)

# 需要找到critical-connections就是需要找不在环上面的边，他们都是critical-connections。
# 所以我们走graph，然后记录rank，如果子节点的rank比当前节点的rank更小，证明当前是环内的连接，连到了原来走过的节点。我们更新当前节点到最小值
# 如果子节点最后的rank是当前rank+1，证明这是一个线性的连接，就是critical-connections

# https://www.youtube.com/watch?v=mKUsbABiwBI

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        g = collections.defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
            
        rank = [-1] * len(connections)
        res = []
        self.dfs(g, rank, 0, 0, -1, res)
        return res
            
    def dfs(self, graph: dict, rank: list, level: int, cur: int, prev: int, res: list) -> int:
        rank[cur] = level
        for child in graph[cur]:
            
            if child == prev:
                # 跳过父节点
                continue
            elif rank[child] == -1:
                # 如果子节点有更小的，意味有一个环，那么当前节点应该选择其中的最小值
                rank[cur] = min(rank[cur], self.dfs(graph, rank, level+1, child, cur, res))
            else:
                # 如果子节点已经走过了，同样：如果子节点有更小的，意味有一个环，那么当前节点应该选择其中的最小值
                rank[cur] = min(rank[cur], rank[child])
                
        # 如果走完了发现rank没变化，证明改连接没有环，就是Critical Connection
        if rank[cur] == level and level != 0:
            res.append([cur, prev])

        return rank[cur]