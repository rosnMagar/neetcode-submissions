import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        # since python heaps are min-heap by default
        h = [[-d[n], n] for n in d.keys()]

        heapq.heapify(h)

        res = []
        for i in range(0, k):
            res.append(heapq.heappop(h)[1] * 1)
        
        return res


