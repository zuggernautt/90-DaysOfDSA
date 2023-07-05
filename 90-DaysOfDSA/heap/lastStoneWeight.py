import heapq

def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            first= -heapq.heappop(max_heap)
            second= -heapq.heappop(max_heap)
            if first!=second:
                heapq.heappush(max_heap,-(first-second))
        if len(max_heap)==1:
            return -max_heap[0]
        else:
            return 0