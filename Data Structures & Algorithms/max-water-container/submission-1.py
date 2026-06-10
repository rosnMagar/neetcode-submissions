class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """
        This is a two pointer problem

        approach: start at either side of the list and find the volume: 
            volume: min(l, r) * r - l
            store the max volume
        find which one is smaller (l or r):
            if it is l increment
            if it is r decrement and run the process again until l == r
        """

        l = 0
        r = len(heights) - 1
        vol = 0

        while l <= r:
            vol = max(vol, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return vol


        