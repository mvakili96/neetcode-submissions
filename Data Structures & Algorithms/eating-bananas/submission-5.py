class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def compute_hours(k,pile):
            return sum((p + k - 1) // k for p in pile)

        l = 1
        r = max(piles)

        while r >= l:
            cen = (r + l) // 2
            duration = compute_hours(cen,piles)

            if duration > h:
                l = cen + 1
            else:
                r = cen - 1

        return l





                


        