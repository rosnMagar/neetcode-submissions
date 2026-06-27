from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 0
            else:
                nums_dict[n] += 1
        nums = [(-nums_dict[key], key) for key in nums_dict]

        heapify(nums)

        res = []
        for j in range(k):
            e = heappop(nums)[1]
            res.append(e)
        
        return res
