class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for c in prerequisites:
            graph[c[0]].extend(c[1:])


        def dfs(course, visited):
            if course in visited:
                return False

            res = True
            visited.add(course)
            for c in graph.get(course, []):
                res = res and dfs(c, visited)
            visited.remove(course)
            return res

        for g in graph.keys():
            visited = set() 
            if not dfs(g, visited):
                return False
        return True