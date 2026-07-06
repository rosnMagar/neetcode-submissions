class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS SOlution

        adj = [[] for _ in range(n)]
        visited = set()

        # both ways for undirected
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i):
            visited.add(i)
            for node in adj[i]:
                if node not in visited:
                    dfs(node)

        res = 0
        for j in range(n):
            if j not in visited:
                dfs(j)
                res += 1
        
        return res





