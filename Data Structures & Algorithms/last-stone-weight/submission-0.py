class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # multiplying by -1 to create a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            if x > y:
                heapq.heappush(stones, -(x - y))

        stones.append(0) 
        return -1 * stones[0]


        