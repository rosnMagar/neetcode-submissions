class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {key: [] for key in range(numCourses)}
        for p in prerequisites:
            adj[p[0]].append(p[1])

        def rec(i, visit):
            if i in visit:
                return False
            visit.add(i)
            res = True
            for j in adj[i]:
                res = res and rec(j, visit)
            visit.remove(i)
            adj[i] = []
            return res

        for k in adj:
            if not rec(k, set()):
                return False

        return True   
            








        
