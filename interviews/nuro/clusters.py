"""
point cluster: 给一个list of points, ex. [0, 1], [0, 2], [0, 3], 还有一个int k. 点跟点距离 less or equal to k 就是在同一个cluster
effect 是transitive. [0, 1], [0, 2] 距离为1, [0,2], [0, 3]距离为1, 所以[0, 1], [0, 2], [0, 3] 在同一个cluster
求总共有几个cluster & 在每个cluster里的点

dbscan algorithm
"""

def find_cluster(arr, k):
    n = len(arr)
    cluster = [i for i in range(n)]
    seen = [False] * n

    for i in range(n):
        if not seen[i]:
            dfs(arr, i, i, cluster, seen, k)

    return cluster


def dfs(arr, i, cur, cluster, seen, k):
    seen[cur] = True
    cluster[cur] = i

    for j in range(len(arr)):
        if not seen[j] and dist(arr[cur], arr[j]) <= k:
            dfs(arr, i, j, cluster, seen, k)


def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

print(find_cluster([[0, 1], [0, 2], [0, 3]], 1))




# another way, union found

def find_cluster_union(arr, k):
    n = len(arr)

    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        p_x = find(x)
        p_y = find(y)
        if p_x != p_y:
            parent[p_x] = p_y

    for i in range(n-1):
        for j in range(i+1, n):
            if dist(arr[i], arr[j]) <= k:
                union(i, j)

    print(parent)

    for i in range(n):
        find(i)

    return parent

print(find_cluster_union([[0, 1], [0, 2], [0, 3]], 1))
    
            