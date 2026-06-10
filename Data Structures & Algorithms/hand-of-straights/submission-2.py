class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1
        
        heap = [key for key in freq.keys()]
        heapq.heapify(heap)

        while heap:
            m = heap[0]
            for i in range(m, m + groupSize):
                if i not in freq.keys():
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True
      