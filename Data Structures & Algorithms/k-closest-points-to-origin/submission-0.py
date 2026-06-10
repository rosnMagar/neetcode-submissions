class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # treating it as a max heap
        distances = [[-(p[0] ** 2 + p[1] ** 2), p[0], p[1]] for p in points]
        heap = []

        for d in distances:
            heapq.heappush(heap, d)
            if len(heap) > k:
                heapq.heappop(heap)
        return [[p[1], p[2]] for p in heap] 