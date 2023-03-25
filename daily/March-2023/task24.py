# 1466. Reorder Routes to Make All Path to the City Zero
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = [[] for i in range(n)]
        for u,v in connections: # adjacency graph; graph[i] contains all neighbours of i node
           graph[u].append(v)
           graph[v].append(-u)
        visited = [0] * n
        return self.dfs(graph, visited, 0)

        
    def dfs(self, graph: list[list[int]], visited: list, root: int):
        cnt = 0
        if not visited[root]:
            visited[root] = 1
        for node in graph[root]:
            if not visited[abs(node)]:
                cnt += self.dfs(graph, visited, abs(node)) + (1 if node > 0 else 0)
        return cnt


print(Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
