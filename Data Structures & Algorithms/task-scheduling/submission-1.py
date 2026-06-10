class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap: 
                m = 1 + heapq.heappop(maxHeap)    
                if m:
                    q.append([m, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
            




        