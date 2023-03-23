# 2492. Minimum Score of a Path Between Two Cities

from collections import defaultdict
from collections import deque

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(dict)
        for a, b, d in roads:
            graph[a][b] = graph[b][a] = d
        min_distance= float('inf')
        visited = set()
        queue = deque([1])
        while queue:
            node1 = queue.popleft()
            for node2, distance in graph[node1].items():
                if node2 not in visited:
                    queue.append(node2)
                    visited.add(node2)
                min_distance = min(min_distance, distance)    
        return min_distance
    
print(Solution().minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
