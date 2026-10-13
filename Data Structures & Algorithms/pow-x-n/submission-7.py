class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) == 1.0:
            if n%2==0:
                return abs(x)
            else:
                return x
        
        if n == 0:
            return 1

        result = 1
        if n < 0:
            n = -1 * n
            x = 1 / x
        
        steps = [n]
        while n > 0:
            steps.append(n//2)
            n = n // 2

        steps = steps[::-1]
        for i in steps:
            result *= result
            if i%2 == 1:
                result *= x

        return result
        