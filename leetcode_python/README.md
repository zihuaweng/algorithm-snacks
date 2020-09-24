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
    - code: graph_topological_sort.py
    
7. [Karnaugh Maps](https://en.wikipedia.org/wiki/Karnaugh_map)
    - The Karnaugh map (KM or K-map) is a method of simplifying Boolean algebra expressions.
    - [video](https://www.youtube.com/watch?v=RO5alU6PpSU)

8. knapsack question
    - select a subset from an array where there sum equals to a target



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
    - graph_strongly_connected_component.py
    - O(V+E)

#### critical connections, bridge
- [video](https://www.youtube.com/watch?v=aZXi1unBdJA)
graph_critical_connections.py
O(V+E)

#### Shortest Path Problem
1. BFS (unweighted graph)
    - O(E + V)
2. Dijkstra's (non-negative acycles)
    - Only works for non-negative weights DAG
    - O(E * logV)
    - code: graph_dijkstra.py
3. Bellman-Ford (negative cycles)
    - works if there is negative weight path, it could use to detect negative cycle
    - O(E * V)
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

#### Topological Sort 
1. Applications:Get the order of graph: class prerequisites, program dependencies. 
1. Does not work for graph with cycle
1. Algorithm 1 dfs:
    1. pick an unvisited node
    2. begin with the selected node, do a dfs, exploring only unvisited nodes.
    3. on the recursive callback of dfs, add the current node to list
    4. reverse the list
1. Algorithm 2 Kahn's Algorithm:
    1. count in degree for all node
    2. add nodes with in degree == 0 to queue
    3. walk throught the queue, add current node to result, decrease the indegree for the next node, if indegree == 0, add to the queue.
1. code: graph_topological_sort.py
1. O(E+V)


### Tree
#### center of undirected tree
[link](https://www.youtube.com/watch?v=nzF_9bjDzdc&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=10)
1. The center is always the middle vertex or middle two vertices in every longest path along the tree.
    - Get the middle of the longest path
2. Another way is to iteratively pick off each leaf node layer like we're peeling an onion.
    - Computer the degree of each node. Each node will have a degree of 1
    - Prune nodes also reduce the node degree
    - tree_find_center.py
3. O(V+E)

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


### 题目总结
1. Complete search
    - Generating subsets: 使用二进制0101011 （ 0:1<<n -1）生成组合，然后生成subset
    - Pruning the search: 矩阵能走过每个点一次的路径数量，可以优化：
        - 只需要走一遍，对称另一边 * 2，确保第一步一定是走同一个方向即可
        - 提前走到终点，该路径不符合条件
        - 如果走到一个点只能选两个方向中一个，证明一定会有另一边的路径不能走到，该路径不符合条件
    - Meet in the middle: 将任务分成两组，对于2^n任务来说可以优化时间


2. Greedy algorithms
Constructs a solution to the problem by always making a choice that looks the best at the moment.
    - Scheduling，计算可以去的最多的meeting：每次选择结束最早的meeting
    - Tasks and deadlines，每次选择耗时最短的
    - Data compression：使用不同长度编码，频率最高的编码成最短的（0），频率较高的编码成较长的（10， 110），但是每个编码不能prefix相同。使用Huffman coding。


3. Dynamic programming
Combines the correctness of complete search and the efficiency of greedy algorithms.

    - 使用场景
        - Finding an optimal solution
        - Counting the number of solutions
        - 下一个结果只依赖前一个结果
    - coin problem：
        - 一组subset的sum需要等于一个target  （从0到target，当前k只会依赖于target-k的结果）
        - 多少组subset的sum可以等于一个target  （从0到target，当前k只会依赖于target-k的结果）
    - Longest increasing subsequence
        - 当前increasing subsequence的长度只取决于前面最大值比他小subset的长度
        - O(nlogn)
    - Paths in a grid
        - 从矩阵的左上角走到右下角，只能往右或者下边走，当前结果只取决于左边结果和上边结果
    - Knapsack problems
        - The term knapsack refers to problems where a set of objects is given, and
subsets with some properties have to be found. 
        - 给一个数组，求出符合条件的subset， [1,3,3,5], 求出sum==12 的subset
        - 每个点都可以选择取或者不取，当前和k （0<k<=sum）只取决于取当前值（k-current）或者不取当前值结果（前一个到达k的结果）
        - possible(x,k) = possible(x−wk,k −1)∨possible(x,k −1)
        - 可以用于计算给定weight，value选择subset
    - Edit distance
        - 当前点只取决于与前一个比较，删减，添加，还是替换
        - distance(a,b) = min(distance(a,b −1)+1, distance(a−1,b)+1, distance(a−1,b −1)+cost(a,b))








