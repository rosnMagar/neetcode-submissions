class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1 --> 3 --> 4 --> 1
        #   --> 2 --> 7 ---> 2
        # 3-->
        #     1 --> 4
        #     2 -->
        
        
        adj = {key: [] for key in range(numCourses)}
        for p in prerequisites:
            adj[p[0]].append(p[1])

        visit = set() 
        def rec(i):
            if i in visit:
                return False
            visit.add(i)
            res = True
            for j in adj[i]:
                res = res and rec(j)
            visit.remove(i)
            return res

        for k in adj:
            visit = set()
            if not rec(k):
                return False

        return True   
            








        
