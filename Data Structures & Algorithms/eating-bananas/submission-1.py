class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left   = 1
        right  = piles[-1]
        answer = right

        while left <= right:
            cen = (left + right) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += pile // cen
                if pile % cen != 0:
                    total_hours += 1

            if total_hours <= h:
                if cen < answer:
                    answer = cen
                right = cen -1 
            else:
                left = cen + 1
            

        return answer



                


        