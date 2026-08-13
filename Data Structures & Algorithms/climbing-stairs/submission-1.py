class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        n_2 = 1
        n_1 = 2

        for i in range(3,n+1):
            out = n_1 + n_2
            n_2 = n_1
            n_1 = out

            
        return out

        