class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = set()

        for v1, v2 in edges:
            # both ways
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(i):
            visited.add(i)
            if adj[i] == []:
                return
            for e in adj[i]:
                if e not in visited:
                    dfs(e)
        
        r = 0
        for e in adj:
            if e in visited:
                continue
            dfs(e)
            r += 1

        return r