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
### Union Find

### Two pointers
