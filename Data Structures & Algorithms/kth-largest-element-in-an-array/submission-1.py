from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-i for i in nums]
        heapify(h) 

        heaped = -1000

        for j in range(0, k):
            heaped = heappop(h)
        
        return -heaped