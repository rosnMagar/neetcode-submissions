class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum: 1 max: max(piles)
        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            i = 0
            for p in piles:
                i += p // m
                if p % m != 0:
                    i += 1
            if i > h:
                l = m + 1
            else:
                r = m - 1
        
        return l