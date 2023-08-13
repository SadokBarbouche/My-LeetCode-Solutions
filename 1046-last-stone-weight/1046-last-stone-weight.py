import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap,-stone)
            
        
        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap) 
            heavier = -heapq.heappop(max_heap) 
            remaining = heaviest - heavier
            heapq.heappush(max_heap, -remaining)
            
        return -max_heap[0] if max_heap else 0
            
            