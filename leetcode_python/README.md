## Algorithm
1. [Rolling Hashing](https://www.youtube.com/watch?v=BQ9E-2umSWc)
2. [Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
    - string-searching algorithm uses hashing to **find an exact match of a pattern string in a text**. It uses a **rolling hash** to quickly filter out positions of the text that cannot match the pattern, and then checks for a match at the remaining positions. Generalizations of the same idea can be used to find more than one match of a single pattern, or to find matches for more than one pattern.
    - two steps: first hashing two substrings, if they have the same hash value, check each character if they match.
3. [Kadane’s Algorithm, DP,](https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d#:~:text=Kadane's%20algorithm%20is%20able%20to,runtime%20of%20O(n).)
    - DP, Maximum Subarray Problem
4. [Floyd's cycle-finding algorithm](https://en.wikipedia.org/wiki/Cycle_detection)
    - Find starting point of cycle / graph
    - Find cycle linked list, find duplicated number in list
    - [explanation video](https://www.youtube.com/watch?v=9YTjXqqJEFE)
5. [Eulerian path](https://en.wikipedia.org/wiki/Eulerian_path#:~:text=An%20Eulerian%20cycle%2C%20Eulerian%20circuit,every%20vertex%20has%20even%20degree.)
    - Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).
    - Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex.
    ```
    Given the graph in the image, is it possible to construct a path (or a cycle; i.e., a path starting and ending on the same vertex) that visits each edge exactly once?
    ```
6. [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
    - A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
    - The graph must be Directed Acyclic Graph (DAG).
    - For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks.
    - Find Eulerian path, school class prerequisites, visit location order
    - code:
    ```python
    class Topological:
        def topological_graph(self, vertices: list) -> list:  # vertices: [[a, b], [b,c]]
            # Build graph
            graph = collections.defaultdict(list)
            for a, b in vertices:
                graph[a].append(b)

            seen = set()
            # Here we can also use stack = collection.deque()
            # and stack.appendleft(i) for adding new elements,
            # and just return stack at the end. O(1)
            stack = []

            for i in range(vertices):
                if i not in seen:
                    self.dfs(graph, i, stack, seen)
            return stack[::-1]

        def dfs(self, graph, i, stack, seen):
            seen.add(i)
            for j in graph[i]:
                if j not in seen:
                    self.dfs(graph, j, stack, seen)
            stack.append(i)
    ```
7. [Karnaugh Maps](https://en.wikipedia.org/wiki/Karnaugh_map)
    - The Karnaugh map (KM or K-map) is a method of simplifying Boolean algebra expressions.
    - [video](https://www.youtube.com/watch?v=RO5alU6PpSU)



## Category
## Union Find
### Union Find by Rank
```python
323. Number of Connected Components in an Undirected Graph

parent = [x for x in range(n)]

def find(x):  
    if parent[x] != x:
        parent[x] = find(parent[x])    # path compression
    return parent[x]

def union(x, y):
    p_x = find(x)
    p_y = find(y)
    if p_x != p_y:               
        parent[p_y] = p_x
        
for u, v in edges:
    union(u, v)
```
Union Find By Rank
```python
parent, rank = {}, {}
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        rank[x] += rank[x] == rank[y]
```
### Graph
#### Representation
1. Adjacency Matrix
##### Pros
- Space efficient for reprenseting dense graphs (have a lot edges)
- Edge weight lookup is O(1)
- Simplest graph representation
##### Cons
- Space O(V^2)
- Iterating over all edges takes O(V^2)

2. Adjacency List
##### Pros
- Space efficient for reprenseting sparse graphs (have a lot nodes)
- Iterating over all edges is efficient
##### Cons
- Less space efficient for reprenseting dense graphs
- Edge lookup is O(E)
- slightly more complex graph representation

#### DFS
1. dfs 一开始就做操作 grid[i][j] = '2' || seen.add(i), 递归的时候判断 边界 + 判断seen + 判断下一个loop条件 grid[x][y] == '1'
```python
200. number of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        grid[i][j] = '2'  # 首先记录seen
        for _x, _y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x = i + _x
            y = j + _y
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':  # 这里因为走过的改成了'2'所以只要判断？= '1'相当于判断了seen和当前val
                self.dfs(grid, x, y)
```
1. 如果dfs需要判断上一层的结果并返回，则把边界放到判断后面，下一个dfs遍历之前。
```python
79. word search

def dfs(self, board, i, j, word):
    if not word:
        return True
    # 因为这里有判断，这个word是又前面的dfs生成的，对边界的判断应该放在最前面，如果没有判断word，例如计算island个数
    # 那样的可以放在生成了新的x,y后面立马判断。
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    if board[i][j] == "#" or board[i][j] != word[0]:  # 判断seen 及条件
        return False
    temp = board[i][j]
    board[i][j] = "#"    # backtrack， 记录seen
    for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
        if self.dfs(board, x, y, word[1:]):
            return True
    board[i][j] = temp
    return FalseF
```

#### Critical Connections
```python
# 需要找到critical-connections就是需要找不在环上面的边，他们都是critical-connections。
# 所以我们走graph，然后记录rank，如果子节点的rank比当前节点的rank更小，证明当前是环内的连接，连到了原来走过的节点。我们更新当前节点到最小值
# 如果子节点最后的rank是当前rank+1，证明这是一个线性的连接，就是critical-connections

# 例子看1192
```

#### Find cycle in directed graph
graph_find_cycle.py

#### strongly connected component
- [video](https://www.youtube.com/watch?v=wUgWX0nc4NY)
1. Tarjan's
    graph_strongly_connected_component.py

#### critical connections, bridge
- [video](https://www.youtube.com/watch?v=aZXi1unBdJA)
graph_critical_connections.py

#### Shortest Path Problem
1. BFS (unweighted graph)
2. Dijkstra's 
3. Bellman-Ford
4. Floyd-Warshall
5. A*

#### Connectivity
1. Union find
2. DFS / BFS

#### Negative Cycles
1. Bellman-Ford
2. Floyd-Warshall

### Traveling Salesman Proble
1. Held-Karp
2. branch and bound


### Tree
#### center of undirected tree
[link](https://www.youtube.com/watch?v=nzF_9bjDzdc&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=10)
1. The center is always the middle vertex or middle two vertices in every longest path along the tree.
    - Get the middle of the longest path
2. Another way is to iteratively pick off each leaf node layer like we're peeling an onion.
    - Computer the degree of each node. Each node will have a degree of 1
    - Prune nodes also reduce the node degree
    - tree_find_center.py

#### Identifying Isomorphic Trees
1. Get the center of both trees
2. Root both trees and encode them.
    1. encode: we use '()' to represent one node. If one node has two children. it should be '(()())', if it only has one child, it should be '(())'. When we create the tree parent encoding, child need to be sorted. '((())())' is corrent but not '(()(()))'
3. Compare the encode tree. We need to root the other tree using all the centers, since we might have two tree center.

```python
def is_isomorphic(tree1, tree2):
    if not tree1 or not tree2:
        return

    center1 = find_tree_center(tree1)
    center2 = find_tree_center(tree2)

    rooted_tree1 = root_tree(tree1, center1[0])  # dosen't matter which center
    encoded_tree1 = encode_tree(rooted_tree1)

    for center in center2:
        rooted_tree2 = root_tree(tree2, center)
        encoded_tree2 = encode_tree(rooted_tree2)
        if encoded_tree1 == encoded_tree2:
            return True
    return False
```


### Two pointers


### Calculate 4 directions
```python
# up
dx, dy = 0, 1
# right
dx, dy = dy, -dx
# left 
dx, dy = -dy, dx
# down
dx, dy = dx, -dy
```

