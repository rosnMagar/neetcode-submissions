class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l <= r:
            k = (r + l) // 2
            t = 0
            for pile in piles:
                t += pile // k
                if pile % k > 0:
                    t += 1
            if t <= h:
                r = k - 1
            elif t > h:
                l = k + 1
        
        return l
