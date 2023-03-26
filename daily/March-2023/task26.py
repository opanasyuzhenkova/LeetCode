class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        def find_loop(root, visited):
            """Find first node belonging to the cycle """
            if visited[root] >= 0:
                return -1
            visited[root] = root
            next = edges[root]
            while next != -1 and visited[next] < 0:
                visited[next] = root
                next = edges[next]
                if next != -1 and visited[next] == root:
                    return next
            return -1
        
        def count_loop(node):
            """Cycle length calculation"""
            next_node = edges[node]
            cnt = 1
            while next_node != node:
                cnt += 1
                next_node = edges[next_node]
            return cnt
        
        n = len(edges)
        visited = [-1] * n
        loop_nodes = []
        for i in range(n):
            node = find_loop(i, visited)
            if node > -1:
                loop_nodes.append(node)

        return max([count_loop(node) for node in loop_nodes], default=-1)
    

print(Solution().longestCycle([3,3,4,2,3]))