class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memoization solution
        cache = [-1] * len(cost)

        def dfs(i):
            if i > len(cost) - 1:
                return 0

            if cache[i] != -1:
                return cache[i]

            m = min(dfs(i + 1), dfs(i + 2)) + cost[i]

            cache[i] = m 
            return m

        dfs(0)
        return min(cache[0], cache[1])

           


        