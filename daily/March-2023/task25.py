# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph

class Solution:
    def countPairs(self, n: int, edges: list[list[int]]):

        def dfs(node) -> int:
            if visited[node]:
                return 0
            visited[node] = True
            cnt = 1
            for v in graph[node]:
                cnt += dfs(v)
            return cnt

        graph = [set() for i in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = [False] * n
        connected_nodes = [0] * n

        for node in range(n):
            if not visited[node]:
                connected_nodes[node] = dfs(node) 
                   
        ans = n * (n - 1) // 2
        for c in connected_nodes:
            ans -= c * (c - 1) // 2
        return ans
    
   
print(Solution().countPairs(n=4, edges=[[0,1],[0,2],[1,2]]))
