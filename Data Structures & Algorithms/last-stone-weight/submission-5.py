import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-item for item in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            res = heapq.heappop(stones) - heapq.heappop(stones)
            heapq.heappush(stones,res)
        return -1*stones[0]
        