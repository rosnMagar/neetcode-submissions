class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        a brute force solution would be to start at each index
        and try to see if we can reach the one before that


        keep track (-1,  -1, -1, 2) ended with a 2
        """
        if sum(gas) < sum(cost):
            return -1
        res = 0 
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res