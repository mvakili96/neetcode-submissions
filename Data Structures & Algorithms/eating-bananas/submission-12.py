class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while r >= l:
            cen = (r + l) // 2
            duration = 0
            for p in piles:
                duration += p//cen
                if p % cen != 0:
                    duration += 1 
            if duration > h:
                l = cen + 1
            else:
                r = cen - 1
        return l





                


        