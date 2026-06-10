class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        visiting = set()

        # first pass to populate the courseMap
        # Map course -> list of indices where this course is the 'dependent' (a)
        for i in range(len(prerequisites)):
            courseMap[prerequisites[i][0]].append(prerequisites[i][1])

        def detectCycle(c):
            if c in visiting:
                return True
            
            if c not in courseMap.keys():
                return False

            visiting.add(c)

            for j in courseMap[c]:
                if detectCycle(j):
                    return True
            
            visiting.remove(c)
            # courseMap[c] = []
            
            return False
        
        for i in range(numCourses):
            if detectCycle(i):
                return False

        return True





