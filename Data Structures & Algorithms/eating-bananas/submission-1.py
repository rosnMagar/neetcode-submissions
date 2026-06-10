class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1, 4, 3, 2    h = 9
        # min and max
        # conduct a binary search between those values
        # find the minimum required value between min and max (rate)
        # using the rate predict the hours required to eat everything
        # if less than h then decrease the rate by shifting the maximum 
        # if more than h then increase the rate by shifting the minimum
        # find a rate where the predicted h = provided h

        # max 4
        # min 1
        # 3 
        # if sum > h then pd_h > 1

        # 10 - 2, 8 - 2, 6 - 2, 4 - 2, 2 - 2

        mn = 1
        mx = max(piles)
        res = mx

        while mn <= mx:
            rate = (mx + mn) // 2
            pd_h = 0

            for pile in piles:
                pd_h += math.ceil(pile / rate)
            
            if pd_h <= h:
                res = rate
                mx = rate - 1
            elif pd_h > h:
                mn = rate + 1
        
        return res
        

            







